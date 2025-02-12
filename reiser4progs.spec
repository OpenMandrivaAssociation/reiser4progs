%define _disable_ld_no_undefined 1

%define major 4
%define api 1.0
%define libname %mklibname %{name}- %{api} %{major}
%define libname_basic %mklibname %{name}-%{api}
%define dev %{_lib}%{name}-devel
%define staticdev %{_lib}%{name}-static-devel
%define minimal_libname %mklibname %{name}-minimal- %{api} 0
%define minimal_libname_basic %mklibname %{name}-minimal-%{api}

Summary:	Utilities belonging to the Reiser4 filesystem
Name:		reiser4progs
Version:	1.0.9
Release:	1
License:	GPL
Group:		System/Kernel and hardware
Source0:	http://cznic.dl.sourceforge.net/project/reiser4/reiser4-utils/reiser4progs/reiser4progs-%{version}.tar.gz
Patch0:		reiser4progs-1.0.7-fix-string-format.patch
URL:		https://www.namesys.com/
BuildRequires:	libaal-static-devel >= 1.0.6
BuildRequires:	glibc-static-devel
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
# wants uuid
BuildRequires:	pkgconfig(ext2fs)
Requires:	%{libname} = %{version}

%description
Reiser4 is a file system using plug-in based object oriented variant
on classical balanced tree algorithms. It is the next generation of
Reiserfs 3.x, the one included in Linux kernel. With new plugins,
people can create their own types of directories and files.

%package -n	%{libname}
Summary:	Libraries needed by Reiser4 programs
Group:		System/Kernel and hardware
Provides:	%{libname_basic} = %{version}-%{release}

%description -n	%{libname}
Libraries needed by Reiser4 programs.

%package -n	%{dev}
Summary:	Development related files for reiser4progs libraries
Group:		Development/Kernel
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{minimal_libname} = %{version}

%description -n %{dev}
Development related files for reiser4progs libraries.

%package -n	%{staticdev}
Summary:	Static reiser4progs libraries
Group:		Development/Kernel
Requires:	%{dev} = %{version}

%description -n	%{staticdev}
Static reiser4progs libraries.

%package -n	%{minimal_libname}
Summary:	Reiser4 library with minimal memory footprint
Group:		System/Kernel and hardware
Provides:	%{minimal_libname_basic} = %{version}-%{release}

%description -n	%{minimal_libname}
This library is another version of Reiser4 library, with minimal
memory footprint.

%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
# be very careful
%configure \
	--sbindir=/sbin \
	--libdir=/%{_lib} \
	--libexecdir=/%{_lib} \
	%{?debug:--enable-debug}

%make

%install
%makeinstall_std

%files
# COPYING contains information other than GPL text
%doc AUTHORS COPYING CREDITS README THANKS
/sbin/*
%{_mandir}/man*/*

%files -n %{libname}
/%{_lib}/libreiser4-%{api}.so.*
/%{_lib}/librepair-%{api}.so.*

%files -n %{minimal_libname}
/%{_lib}/libreiser4-minimal-%{api}.so.*

%files -n %{dev}
%doc BUGS ChangeLog TODO
/%{_lib}/lib*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4

%files -n %{staticdev}
/%{_lib}/lib*.a
