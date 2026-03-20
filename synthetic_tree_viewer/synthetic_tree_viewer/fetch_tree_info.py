#!/usr/bin/env python
import requests
import logging
import json
from .util import get_opentree_api_endpoints

log = logging.getLogger(__name__)

_draft_tree_name, _start_node_id = None, None


def fetch_current_synthetic_tree_ids(request):
    """Returns the latest synthetic-tree ID and its root node ID. Cached."""
    global _draft_tree_name, _start_node_id
    if (_draft_tree_name is not None) and (_start_node_id is not None):
        return _draft_tree_name, _start_node_id
    log.debug("Fetching _draft_tree_name, _start_node_id ")
    # Get the URL of the tree API server
    method_dict = get_opentree_api_endpoints(request)
    fetch_url = method_dict["getDraftTreeID_url"]
    # this needs to be a POST (pass fetch_args or ''); if GET, it just describes the API
    ids_json = requests.post(
        url=fetch_url,
        data=json.dumps({}),
        headers={"Content-Type": "application/json"},
    ).json()
    _draft_tree_name = str(ids_json["synth_id"])
    _start_node_id = str(ids_json["root"]["node_id"])
    msg = f"_draft_tree_name = {_draft_tree_name} _start_node_id={_start_node_id}"
    log.debug(msg)
    return _draft_tree_name, _start_node_id
