from conans import ConanFile, CMake


class PocoTestConan(ConanFile):
    name = "poco_test"
    version = "0.1"

    license = "<MIT>"
    author = "<Samuel Zhang>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Just a demo app for Poco and cpprestsdk>"
    
    topics = ("Poco", "cpprest", "http")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}

    generators = "cmake"
    exports_sources = "src/*"

    # requires = "Poco/1.10.1@pocoproject/stable", "cpprestsdk/2.10.18@pocoproject/stable"
    requires = "Poco/1.10.1@pocoproject/stable"


    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
