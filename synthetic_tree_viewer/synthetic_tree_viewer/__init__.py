from pyramid.config import Configurator

# Use Pyramid's default cookie session implementation
# see <https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/sessions.html#using-the-default-session-factory>
from pyramid.session import SignedCookieSessionFactory
import logging
from .fetch_tree_info import fetch_current_synthetic_tree_ids
from .tree_view_dict_mgr import create_tree_view_dict

log = logging.getLogger(__name__)

my_session_factory = SignedCookieSessionFactory("secret sauce")


def create_api_endpoints(rset):
    # @TODO implement scheme relative URLs? not done here
    #   MTH stripped out that logic because I think it is an old
    #   web2py ini option
    try:
        default_apis = rset["api_base_urls.default_apis"]
        production_apis = rset["api_base_urls.production_apis"]
    except KeyError:
        raise RuntimeError(
            "api_base_urls.default_apis and api_base_urls.production_apis must be found in ini file."
        )
    while default_apis.endswith("/"):
        default_apis = default_apis[:-1]
    while production_apis.endswith("/"):
        production_apis = production_apis[:-1]
    cached_default_apis = f"{default_apis}/cached"
    cached_production_apis = f"{production_apis}/cached"
    aeps = {}
    aeps["getDraftTreeID_url"] = f"{default_apis}/v3/tree_of_life/about"
    aeps["getSyntheticTree_url"] = f"{cached_default_apis}/v3/tree_of_life/subtree"
    aeps["getDraftSubtree_url"] = f"{default_apis}/v3/tree_of_life/subtree"
    aeps["doTNRSForAutocomplete_url"] = f"{default_apis}/v3/tnrs/autocomplete_name"
    aeps["getContextsJSON_url"] = f"{cached_default_apis}/v3/tnrs/contexts"
    aeps["getSynthesisSourceList_url"] = f"{cached_default_apis}/v3/tree_of_life/about"
    aeps["findAllStudies_url"] = f"{cached_production_apis}/v3/studies/find_studies"
    aeps["singlePropertySearchForStudies_url"] = (
        f"{production_apis}/v3/studies/find_studies"
    )
    aeps["singlePropertySearchForTrees_url"] = (
        f"{production_apis}/v3/studies/find_trees"
    )
    aeps["getTaxonInfo_url"] = f"{default_apis}/v3/taxonomy/taxon_info"
    rset["api_endpoints"] = aeps
    return aeps


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    with Configurator(settings=settings) as config:
        ## Allow subrequests in your Pyramid application.
        # config.add_subrequest_handler()
        # Is this deprecated?!
        config.set_session_factory(my_session_factory)
        config.include("pyramid_jinja2")
        config.include("pyramid_retry")
        config.include(".routes")
        config.scan()
        rset = config.registry.settings
        aeps = create_api_endpoints(rset)
        tvd = create_tree_view_dict(rset)
        tvd.update(aeps)

        # rset["path_to_app_config_sp"] = rset["path_to_app_config"].split()
    log.debug("Configured. Calling make_wsgi_app...")
    return config.make_wsgi_app()
