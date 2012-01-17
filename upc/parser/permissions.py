from upc.parser.parser import parser

class permissions(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb_local = kb.register_section("permissions")
		self.kb_global = kb
		self.kb_local.register_string("filename")
		self.kb_local.add_info("filename", filename)
		
		#fsobjs = self.query_perms(filename, {"matches": ["world_writeable"]})
		
		for f in self.query_perms(filename, {"min_size": 500000, "matches": ["file", "world_readable"]}):
			self.report.get_by_id("UPC519").add_supporting_data('text_line', [self.kb_global, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["world_writeable", "directory"], "ignore": ["sticky"]}):
			self.report.get_by_id("UPC513").add_supporting_data('text_line', [self.kb_global, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["world_writeable", "file"]}):
			c = self.report.get_by_id("UPC518").count_supporting_data('text_line')
			if c < 200:
				self.report.get_by_id("UPC518").add_supporting_data('text_line', [self.kb_global, f.get_line()])
			elif c == 200:
				self.report.get_by_id("UPC518").add_supporting_data('text_line', [self.kb_global, "... Only first 200 listed ..."])

		for f in self.query_perms(filename, {"matches": ["world_writeable", "directory", "sticky"]}):
			self.report.get_by_id("UPC514").add_supporting_data('text_line', [self.kb_global, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["suid", "file"]}):
			self.report.get_by_id("UPC515").add_supporting_data('text_line', [self.kb_global, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["sgid", "file"]}):
			self.report.get_by_id("UPC516").add_supporting_data('text_line', [self.kb_global, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["sgid", "directory"]}):
			self.report.get_by_id("UPC517").add_supporting_data('text_line', [self.kb_global, f.get_line()])

		# world writeable files
		# world writeable directories
		# readable big file
		# writeable home directories