RVL_OPTS = '-ipa file'
EGG_OPTS = '-ipa function -rostr'
REL_OPTS = '-ipa file -rostr -sdata 0 -sdata2 0'

compile_source("source/rvl/arc/rvlArchive.c", "out/rvlArchive.o", '4199_60831', RVL_OPTS)
compile_source("source/rvl/mem/rvlMemList.c", "out/rvlMemList.o", '4199_60831', RVL_OPTS)

compile_source("source/dwc/common/dwc_error.c", "out/dwc_error.o", '4199_60831', RVL_OPTS)

compile_source("source/egg/core/eggAllocator.cpp", "out/eggAllocator.o", '4201_127', EGG_OPTS + " -use_lmw_stmw=on ")
compile_source("source/egg/core/eggArchive.cpp", "out/eggArchive.o", '4201_127', EGG_OPTS + " -use_lmw_stmw=on ")
compile_source("source/egg/core/eggDisposer.cpp", "out/eggDisposer.o", '4201_127', EGG_OPTS)
compile_source("source/egg/core/eggGraphicsFifo.cpp", "out/eggGraphicsFifo.o", '4201_127', EGG_OPTS)
compile_source("source/egg/core/eggHeap.cpp", "out/eggHeap.o", '4201_127', EGG_OPTS + " -ipa file -use_lmw_stmw=on  ")
compile_source("source/egg/math/eggQuat.cpp", "out/eggQuat.o", '4201_127', EGG_OPTS)
compile_source("source/egg/core/eggStreamDecomp.cpp", "out/eggStreamDecomp.o", '4201_127', EGG_OPTS)
# compile_source("source/egg/core/eggSystem.cpp", "out/eggSystem.o", '4201_127', EGG_OPTS)
compile_source("source/egg/core/eggThread.cpp", "out/eggThread.o", '4201_127', EGG_OPTS)
compile_source("source/egg/core/eggUnitHeap.cpp", "out/eggUnitHeap.o", '4201_127', EGG_OPTS + " -use_lmw_stmw=on  ")
compile_source("source/egg/math/eggVector.cpp", "out/eggVector.o", '4201_127', EGG_OPTS)
# compile_source("source/egg/core/eggXfb.cpp", "out/eggXfb.o", '4201_127', EGG_OPTS)
# compile_source("source/egg/core/eggXfbManager.cpp", "out/eggXfbManager.o", '4201_127', EGG_OPTS)

compile_source("source/game/ui/MessageGroup.cpp", "out/MessageGroup.o", '4201_127', EGG_OPTS)
compile_source("source/game/jmap/JmpResourceCourse.cpp", "out/JmpResourceCourse.o", '4201_127', REL_OPTS)