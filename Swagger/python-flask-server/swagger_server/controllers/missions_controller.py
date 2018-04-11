import connexion
import six

from swagger_server.models.endpoints import Endpoints  # noqa: E501
from swagger_server.models.filelist import Filelist  # noqa: E501
from swagger_server.models.missions import Missions  # noqa: E501
from swagger_server import util, missions_readable, missions_true
import os


def get_home_naif():  # noqa: E501
    """List of available missions in naif format

     # noqa: E501


    :rtype: List[Missions]
    """
    human_read = []

    for miss in os.listdir('/app/'):
        if miss[0] == '.':
            continue
        else:
            human_read.append(miss)
    return human_read


def get_misc(mission):  # noqa: E501
    """List of the available misc. files for a given mission

     # noqa: E501

    :param mission:
    :type mission: str

    :rtype: List[Filelist]
    """
    return 'do some magic!'


def get_mission_endpoints(mission):  # noqa: E501
    """List of the available endpoints for a given mission

     # noqa: E501

    :param mission:
    :type mission: str

    :rtype: List[Endpoints]
    """
    endpoints = ['/kernels', '/misc', '/metakernels']
    return endpoints


def get_missions():  # noqa: E501
    """List of available missions (Human-Readable)

     # noqa: E501


    :rtype: List[Missions]
    """
    human_read = []
    for miss in os.listdir('/app/'):
        if miss[0] == '.':
            continue
        else:
            human_read.append(missions_readable[miss])
    return human_read
