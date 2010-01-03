#python

import k3d
import testing

setup = testing.setup_mesh_reader_test("PLYMeshReader", "mesh.modifier.PGPRemesh.bunny.ply")

modifier = setup.document.new_node("PGPRemesh")
modifier.use_smooth = True
modifier.steps = 1
modifier.h = 100000
modifier.omega = 10
modifier.div = 10
modifier.triangulate = True
document.set_dependency(modifier.get_property("input_mesh"), setup.source.get_property("output_mesh"))

#print "source output: " + repr(source.output_mesh)
#print "triangles output: " + repr(triangles.output_mesh)
#print "modifier output: " + repr(modifier.output_mesh)

testing.require_valid_primitives(document, modifier.get_property("output_mesh"))
testing.mesh_reference_comparison(document, modifier.get_property("output_mesh"), "mesh.modifier.PGPRemesh.bunny", 1)

