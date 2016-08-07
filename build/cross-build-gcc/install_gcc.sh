#!/bin/sh
ins_dir=
target=x86_64-linux
kernel_inc_path=/usr/src/kernels/`uname -r`
arch=x86_64-linux

binutils_dir=binutils-2.27
binutils=$binutils_dir.tar.gz

glibc_dir=glibc-2.24
glibc=$glibc_dir.tar.gz
linuxthreads_pkg=glibc-linuxthreads-2.3.tar.gz

gcc_all_pkg=gcc-install-pack.tar.gz

gcc_dir=gcc-4.8.5
gcc_pkg=$gcc_dir.tar.gz

gmp_dir=gmp-4.3.2
gmp_pkg=$gmp_dir.tar.gz

mpc_dir=mpc-1.0.3
mpc_pkg=$mpc_dir.tar.gz

mpfr_dir=mpfr-3.1.4
mpfr_pkg=$mpfr_dir.tar.gz

if [ $# -le 1 ]
then
    echo 'please input install dir'
    echo 'example:./install-gcc.sh -d /work/x86_64_linux'
    exit 1
fi

#获取安装目录及对象名，默认对象名为x86_64_linux
while [ $# -ne 0 ]
do 
    if [ $1 == '-d' ]
    then    
        ins_dir=$2
        shift;
    elif [ $1 == '-t' ]
    then
        target=$2
        echo "target is $target"
        shift;
    elif [ $1 == '-a' ]
    then    
        arch=$2
        echo "arch is $arch"
        shift;
    fi
    
    shift;
done


#export 环境变量
export PRJROOT=$ins_dir
export TARGET=$target
export PREFIX=$PRJROOT/tools
export TARGET_PREFIX=$PREFIX/$TARGET
export PATH=$PATH:$PREFIX/bin/sh

#创建安装目录
mkdir $ins_dir -p
cd $ins_dir
mkdir build-tools tools
cd -

#拷贝并解压
cp ./$binutils $ins_dir/build-tools
cd $ins_dir/build-tools
tar xvf $binutils
rm $binutils
cd -

cp ./$glibc $ins_dir/build-tools
#cp ./$linuxthreads_pkg $ ins_dir/build-tools
cd $ins_dir/build-tools
tar xvf ./$glibc
#tar xvf ./$linuxthreads_pkg --directory=$glibc_dir
rm ./$glibc
#rm ./$linuxthreads_pkg
cd -

cp ./$gcc_all_pkg $ins_dir/build-tools
cd $ins_dir/build-tools
tar xvf ./$gcc_all_pkg
rm ./$gcc_all_pkg

tar xvf ./$gcc_pkg
tar xvf $gmp_pkg -C $gcc_dir/
tar xvf $mpc_pkg -C $gcc_dir/
tar xvf $mpfr_pkg -C $gcc_dir/

cd $ins_dir/build-tools/$gcc_dir
ln -sf $gmp_dir gmp
ln -sf $mpc_dir mpc
ln -sf $mpfr_dir mpfr

cd $ins_dir/build-tools
rm $gmp_pkg
rm $mpc_pkg
rm $mpfr_pkg
rm $gcc_pkg

#编译安装binutils
cd $ins_dir/build-tools
mkdir build$binutils_dir -p
cd build$binutils_dir
../$binutils_dir/configure --target=$TARGET --prefix=$PREFIX
make all -j4
make install
#编译安装gcc
cd  $ins_dir/build-tools
mkdir build$gcc_dir -p
cd build$gcc_dir
../$gcc_dir/configure --target=$TARGET --prefix=$PREFIX --without-headers --enable-languages=c --disable-threads --with-newlib --disable-shared --disable-libmudflap --disable-libssp --disable-decimal-float --disable-multilib
make all-gcc -j4; 
make install-gcc -j4;
make all-target-libgcc -j4
make install-target-libgcc -j4

#拷贝内核头文件
#此处注意一下
cp -fr /usr/include/ $TARGET_PREFIX/include
cp $TARGET_PREFIX/include/x86_64-linux-gnu/asm $TARGET_PREFIX/include -fr

#编译安装glibc
cd $ins_dir/build-tools
mkdir build$glibc_dir -p
cd build$glibc_dir
CC=$TARGET-gcc
$ins_dir/build-tools/$glibc_dir/configure --host=$TARGET --target=$TARGET --prefix=$TARGET_PREFIX  --disable-profile  --with-binutils=$PREFIX/bin --with-headers=$TARGET_PREFIX/include --disable-multilib
make all -j4;
make install -j4
#编译安装gcc
cd $ins_dir/build-tools/build$gcc_dir
rm -rf *
../$gcc_dir/configure --prefix=$PREFIX --target=$TARGET --enable-shared --enable-languages=c,c++ --disable-multilib
make all -j4
make install

















































































