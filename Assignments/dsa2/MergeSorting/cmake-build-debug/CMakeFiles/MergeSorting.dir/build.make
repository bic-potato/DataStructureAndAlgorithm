# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/zuoxichen/clion-2020.3.3/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/zuoxichen/clion-2020.3.3/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/MergeSorting.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/MergeSorting.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/MergeSorting.dir/flags.make

CMakeFiles/MergeSorting.dir/MergeSort.cpp.o: CMakeFiles/MergeSorting.dir/flags.make
CMakeFiles/MergeSorting.dir/MergeSort.cpp.o: ../MergeSort.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/MergeSorting.dir/MergeSort.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/MergeSorting.dir/MergeSort.cpp.o -c /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/MergeSort.cpp

CMakeFiles/MergeSorting.dir/MergeSort.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MergeSorting.dir/MergeSort.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/MergeSort.cpp > CMakeFiles/MergeSorting.dir/MergeSort.cpp.i

CMakeFiles/MergeSorting.dir/MergeSort.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MergeSorting.dir/MergeSort.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/MergeSort.cpp -o CMakeFiles/MergeSorting.dir/MergeSort.cpp.s

# Object files for target MergeSorting
MergeSorting_OBJECTS = \
"CMakeFiles/MergeSorting.dir/MergeSort.cpp.o"

# External object files for target MergeSorting
MergeSorting_EXTERNAL_OBJECTS =

libMergeSorting.so: CMakeFiles/MergeSorting.dir/MergeSort.cpp.o
libMergeSorting.so: CMakeFiles/MergeSorting.dir/build.make
libMergeSorting.so: CMakeFiles/MergeSorting.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libMergeSorting.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MergeSorting.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/MergeSorting.dir/build: libMergeSorting.so

.PHONY : CMakeFiles/MergeSorting.dir/build

CMakeFiles/MergeSorting.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/MergeSorting.dir/cmake_clean.cmake
.PHONY : CMakeFiles/MergeSorting.dir/clean

CMakeFiles/MergeSorting.dir/depend:
	cd /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/cmake-build-debug /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/cmake-build-debug /home/zuoxichen/Documents/DataStructureAndAlgorithm/Assignments/dsa2/MergeSorting/cmake-build-debug/CMakeFiles/MergeSorting.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/MergeSorting.dir/depend
