import mama

class ExampleRemote(mama.BuildTarget):
    
    def dependencies(self):
        self.set_build_dependency("bin/ExampleRemote.lib")

    def build(self):
        pass

    def package(self):
        self.export_includes(".")
        self.export_libs("bin")
