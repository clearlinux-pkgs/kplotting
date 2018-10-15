#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kplotting
Version  : 5.51.0
Release  : 5
URL      : https://download.kde.org/stable/frameworks/5.51/kplotting-5.51.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.51/kplotting-5.51.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.51/kplotting-5.51.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kplotting-lib = %{version}-%{release}
Requires: kplotting-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# KPlotting
Data plotting
## Introduction
KPlotWidget is a QWidget-derived class that provides a virtual base class
for easy data-plotting. The idea behind KPlotWidget is that you only have
to specify information in "data units"; i.e., the natural units of the
data being plotted.  KPlotWidget automatically converts everything
to screen pixel units.

%package dev
Summary: dev components for the kplotting package.
Group: Development
Requires: kplotting-lib = %{version}-%{release}
Provides: kplotting-devel = %{version}-%{release}

%description dev
dev components for the kplotting package.


%package lib
Summary: lib components for the kplotting package.
Group: Libraries
Requires: kplotting-license = %{version}-%{release}

%description lib
lib components for the kplotting package.


%package license
Summary: license components for the kplotting package.
Group: Default

%description license
license components for the kplotting package.


%prep
%setup -q -n kplotting-5.51.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539617394
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1539617394
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kplotting
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kplotting/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KPlotting/KPlotAxis
/usr/include/KF5/KPlotting/KPlotObject
/usr/include/KF5/KPlotting/KPlotPoint
/usr/include/KF5/KPlotting/KPlotWidget
/usr/include/KF5/KPlotting/kplotaxis.h
/usr/include/KF5/KPlotting/kplotobject.h
/usr/include/KF5/KPlotting/kplotpoint.h
/usr/include/KF5/KPlotting/kplotting_export.h
/usr/include/KF5/KPlotting/kplotwidget.h
/usr/include/KF5/kplotting_version.h
/usr/lib64/cmake/KF5Plotting/KF5PlottingConfig.cmake
/usr/lib64/cmake/KF5Plotting/KF5PlottingConfigVersion.cmake
/usr/lib64/cmake/KF5Plotting/KF5PlottingTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Plotting/KF5PlottingTargets.cmake
/usr/lib64/libKF5Plotting.so
/usr/lib64/qt5/mkspecs/modules/qt_KPlotting.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Plotting.so.5
/usr/lib64/libKF5Plotting.so.5.51.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kplotting/COPYING.LIB
