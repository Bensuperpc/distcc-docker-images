#git clone https://github.com/llvm/llvm-project.git build/llvm-project/
export LOCAL_DISTCC_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' localdistcc)
export DISTCC_HOSTS="$LOCAL_DISTCC_IP/7 localhost"
#export DISTCC_HOSTS="fasthost/8 slowhost/2 localhost"
mkdir -p build/llvm-builds/release-gcc-distcc
cd build/llvm-builds/release-gcc-distcc
cmake ../../llvm-project/llvm \
  -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DLLVM_USE_LINKER=gold \
  -DLLVM_ENABLE_PROJECTS="lldb;clang;lld" \
  -DCMAKE_C_COMPILER=/usr/bin/gcc \
  -DCMAKE_CXX_COMPILER=/usr/bin/g++ \
  -DCMAKE_EXPORT_COMPILE_COMMANDS=1 \
  -DCMAKE_C_COMPILER_LAUNCHER="ccache;distcc" \
  -DCMAKE_CXX_COMPILER_LAUNCHER="ccache;distcc"
ninja lldb -j $(distcc -j)