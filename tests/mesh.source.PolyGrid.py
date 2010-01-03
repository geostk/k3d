#python

import testing

setup = testing.setup_mesh_source_test("PolyGrid")

testing.require_valid_primitives(setup.document, setup.source.get_property("output_mesh"))
testing.mesh_reference_comparison(setup.document, setup.source.get_property("output_mesh"), "mesh.source.PolyGrid", 1, testing.platform_specific)

