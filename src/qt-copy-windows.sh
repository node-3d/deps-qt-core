# $1 is tmp path - ${{ github.workspace }}/../__tmp
# $2 is Qt platform path - /home/opc/6.8.0/gcc_arm64

# Core
cp $2/bin/Qt6Core.dll $1/Qt6Core.dll
cp $2/bin/Qt6Network.dll $1/Qt6Network.dll
cp $2/plugins/platforms/qminimal.dll $1/plugins/platforms/qminimal.dll
