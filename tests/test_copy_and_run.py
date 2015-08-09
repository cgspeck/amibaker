import pytest
# - check copy call
# - check sudo | run call
# + args
# - check delete call

BASIC_TEMPLATE = {'from':'/some/script'}

BASIC_TEMPLATE_ARGS = {'from':'/some/script', 'args':'foo --bar=true baz=3'}

@pytest.mark.parametrize("input", [
    []  # empty list,
    [BASIC_TEMPLATE],  # one basic call
    [BASIC_TEMPLATE, BASIC_TEMPLATE],  # two basic calls
    [{'sudo':True}.update(BASIC_TEMPLATE_ARGS)],
    [{'sudo':True}.update(BASIC_TEMPLATE)]
])
def test_copy_and_run(input):
    pass



@pytest.mark.parametrize("input", [
    []  # empty list,
    [{'post_provisioning':False}.update(BASIC_TEMPLATE)],  # this is default behaviour
    [{'post_provisioning':True}.update(BASIC_TEMPLATE)],  # after provisioning script
    [{'post_provisioning':False}.update(BASIC_TEMPLATE), {'post_provisioning':True}.update(BASIC_TEMPLATE)],  # after provisioning script
])
def test_sequencing(input):
    pass
