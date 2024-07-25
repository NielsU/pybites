import os
import dataclasses
from pathlib import Path
from ipaddress import IPv4Network
from urllib.request import urlretrieve

import pytest

from ips import ServiceIPRange, parse_ipv4_service_ranges, get_aws_service_range

URL = "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "ip-ranges.json")
IP = IPv4Network("192.0.2.8/29")


@pytest.fixture(scope="module")
def json_file():
    """Import data into tmp folder"""
    urlretrieve(URL, PATH)
    return PATH


# Didnt have to be a fixture i guess, could be just a function.
@pytest.fixture(scope="module")
def sip_range_amazon_euwest2():
    return ServiceIPRange(
        service="AMAZON", region="eu-west-2", cidr=IPv4Network("54.239.0.240/28")
    )


# test cases:
def test_ServiceIPRange_Class(sip_range_amazon_euwest2):

    assert type(sip_range_amazon_euwest2) is ServiceIPRange

    assert (
        str(sip_range_amazon_euwest2)
        == "54.239.0.240/28 is allocated to the AMAZON service in the eu-west-2 region"
    )


def test_ServiceIPRange_data_class_should_be_frozen(sip_range_amazon_euwest2):
    with pytest.raises(dataclasses.FrozenInstanceError):
        sip_range_amazon_euwest2.service = "SOME_OTHER_SERVICE"


# Not sure if this fixture is a smart idea in practice.
# Have created it to share the parsed json result over multple tests. but since this is the code tested
# Perhaps its better not to separate running the tested code in setup scope?
@pytest.fixture(scope="module")
def ip4_service_ranges_list(json_file):
    return parse_ipv4_service_ranges(json_file)


def test_parse_ipv4_service_ranges_return_type(ip4_service_ranges_list):

    assert isinstance(ip4_service_ranges_list, list)

    assert all(isinstance(item, ServiceIPRange) for item in ip4_service_ranges_list)


def test_parse_ipv4_service_ranges_ip_list_data_content(
    sip_range_amazon_euwest2, ip4_service_ranges_list
):
    assert len(ip4_service_ranges_list) == 1886

    assert sip_range_amazon_euwest2 in ip4_service_ranges_list


@pytest.mark.parametrize(
    "address",
    [
        "54.239.0.241",
        "54.239.0.242",
        "54.239.0.243",
        "54.239.0.244",
        "54.239.0.245",
        "54.239.0.246",
        "54.239.0.247",
        "54.239.0.248",
    ],
)
def test_get_aws_service_ip_in_euwest2_range(address, request):
    input_ranges_list = request.getfixturevalue("ip4_service_ranges_list")
    output_ranges_list = [request.getfixturevalue("sip_range_amazon_euwest2")]
    assert get_aws_service_range(address, input_ranges_list) == output_ranges_list


@pytest.mark.parametrize(
    "address",
    [
        "0.0.0.0",
        "10.0.0.1",
        "192.168.2.1",
    ],
)
def test_get_aws_service_ip_no_match(address, ip4_service_ranges_list):
    assert get_aws_service_range(address, ip4_service_ranges_list) == []


def test_get_aws_service_invalid_ip_address_raises_value_error():
    with pytest.raises(ValueError):
        address = "not an ip"
        input_ranges_list = []
        get_aws_service_range(address, input_ranges_list)


def test_get_aws_service_invalid_ip_address_verify_error_message():
    address = "not an ip"
    input_ranges_list = []
    try:
        get_aws_service_range(address, input_ranges_list)
    except ValueError as e:
        assert str(e) == "Address must be a valid IPv4 address"


def test_get_aws_service_non_iterable_service_range():
    # to verify invalid input raises error.
    with pytest.raises(TypeError):
        address = "192.168.2.1"
        service_ranges_list = 10
        get_aws_service_range(address, service_ranges_list)


def test_get_aws_service_service_range_invalid_attribute():
    # to verify invalid input raises error.
    with pytest.raises(AttributeError):
        address = "192.168.2.1"
        service_ranges_list = "string is not a service ip range type"
        get_aws_service_range(address, service_ranges_list)
