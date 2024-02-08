# Maintainer: Antonio Rojas <arojas@archlinux.org>

_name=kholidays
pkgname=${_name}5-cn
pkgver=5.114.0
pkgrel=1
epoch=1
pkgdesc='KDE library for regional holiday information(CN)'
arch=(x86_64)
url='https://community.kde.org/Frameworks'
license=(LGPL)
depends=(qt5-base)
makedepends=(extra-cmake-modules qt5-declarative qt5-tools qt5-doc doxygen python)
optdepends=('qt5-declarative: QML bindings')
conflicts=("$_name<1:5.111" "kholidays5")
replaces=("$_name<1:5.111" "kholidays5")
provides=("kholidays5")
groups=(kf5)
source=(https://download.kde.org/stable/frameworks/${pkgver%.*}/$_name-$pkgver.tar.xz git+https://github.com/0xcccccccccccc/kholidays_cn.git)
sha256sums=('SKIP')

build() {
  cp $startdir/holiday_cn_zh-cn $srcdir/kholidays-$pkgver/holidays/plan2/
  cmake -B build -S $_name-$pkgver \
    -DBUILD_TESTING=OFF \
    -DBUILD_QCH=ON
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
