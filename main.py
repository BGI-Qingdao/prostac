"""this is an example to run on 192.168.66.203"""
import get_alignments
pdb_path = '/dellfsqd2/ST_OCEAN/USER/wangdantong/python_toolbox_test/prostac/pdb_files'
us_path = '/dellfsqd2/ST_OCEAN/USER/wangdantong/toolboxes/usalign/USalign/USalign'
parallel = 1
#get_alignments.run_usalign(pdb_path, us_path, parallel)
get_alignments.cat_align(pdb_path, us_path)