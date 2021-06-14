
from HTTPSession import HTTPSession
from multiprocessing import Pool, Process, Queue
import json
import hashlib
import base64
import time

def post_hash(password, queue=None):
    """
    Function to submit POST request to hash endpoint.
    Args:
        password (str): Password to be hashed and ecoded.
        queue (obj): Multiprocessing queue object to hold response object
    Returns:
        resp (obj): Response object from POST request
    """

    http_session = HTTPSession()
    endpoint = '/hash'
    params = {
        'password' : password
    }

    resp = http_session.rs.post(http_session.baseurl + endpoint, json=params)

    if queue is not None:
        queue.put(resp)
    else:
        return resp

def get_hash(job_id):
    """
    Function to submit GET request to hash endpoint.
    Args:
        job_id (str): Job ID that links POST request to encoded password hash.
    Returns:
        resp (obj): Response object from GET request
    """

    time.sleep(7)

    http_session = HTTPSession()
    endpoint = '/hash'

    resp = http_session.rs.get(http_session.baseurl + endpoint + '/' + job_id)

    return resp

def get_stats():
    """
    Function to submit GET request to stats endpoint.
    Args:
    Returns:
        resp (obj): Response object from GET request
    """

    http_session = HTTPSession()
    endpoint = '/stats'

    resp = http_session.rs.get(http_session.baseurl + endpoint)

    return resp

def shutdown(queue=None):
    """
    Function to submit Shutdown request to hash endpoint.
    Args:
        queue (obj): Multiprocessing queue object to hold response object
    Returns:
        resp (obj): Response object from POST request
    """

    http_session = HTTPSession()
    endpoint = '/hash'
    data = 'shutdown'

    resp = http_session.rs.post(http_session.baseurl + endpoint, data=data)

    if queue is not None:
        queue.put(resp)
    else:
        return resp

    def test_post_hash_successful(password):
        """
        Test to check that POST request to hash endpoint is successful
        Args:
            password (str): Password to be hashed and ecoded.
        Returns:
        """

        resp = post_hash(password)

        if (resp.status_code >= 300 or resp.status_code < 200):
            print
            'FAIL: test_post_hash_successful'
            print
            'Expected Status Code: 2xx'
            print
            'Actual Status Code: ' + str(resp.status_code)
        else:
            print
            'PASS: test_post_hash_successful'

    def test_get_hash_successful(password):
        """
        Test to check that GET request to hash endpoint is successful
        Args:
            password (str): Password to be hashed and ecoded.
        Returns:
        """

        post_resp = post_hash(password)
        get_resp = get_hash(post_resp.text)

        if (get_resp.status_code >= 300 or get_resp.status_code < 200):
            print
            'FAIL: test_get_hash_successful'
            print
            'Expected Status Code: 2xx'
            print
            'Actual Error Code: ' + str(get_resp.status_code)
        else:
            print
            'PASS: test_get_hash_successful'

    def test_get_stats_successful():
        """
        Test to check that GET request to stats endpoint is successful
        Args:
        Returns:
        """

        resp = get_stats()

        if (resp.status_code >= 300 or resp.status_code < 200):
            print
            'FAIL: test_get_stats_successful'
            print
            'Expected Status Code: 2xx'
            print
            'Actual Error Code: ' + str(resp.status_code)
        else:
            print
            'PASS: test_get_stats_successful'

    def test_shutdown_successful():
        """
        Test to check that shutting down is successful
        Args:
        Returns:
        """

        resp = shutdown()

        if (resp.status_code >= 300 or resp.status_code < 200):
            print
            'FAIL: test_shutdown_successful'
            print
            'Expected Status Code: 2xx'
            print
            'Actual Status Code: ' + str(resp.status_code)
        else:
            print
            'PASS: test_shutdown_successful'