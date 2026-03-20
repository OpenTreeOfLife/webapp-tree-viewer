#!/usr/bin/env python
import requests
import logging
import json
from .util import get_opentree_api_endpoints

log = logging.getLogger(__name__)

_draft_tree_name, _start_node_id = None, None


def fetch_current_synthetic_tree_ids(request):
    global _draft_tree_name, _start_node_id
    if (_draft_tree_name is not None) and (_start_node_id is not None):
        return _draft_tree_name, _start_node_id
    log.debug("Fetching _draft_tree_name, _start_node_id ")
    # return the latest synthetic-tree ID (and its 'life' node ID)
    try:
        # fetch the latest IDs as JSON from remote site

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
        log.debug(
            f"_draft_tree_name = {_draft_tree_name} _start_node_id={_start_node_id}"
        )
        return _draft_tree_name, _start_node_id
    except Exception as e:
        # throw 403 or 500 or just leave it
        return "ERROR", str(e)
