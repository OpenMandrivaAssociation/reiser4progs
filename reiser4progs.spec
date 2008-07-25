%define name	reiser4progs
%define version 1.0.4
%define release %mkrel 3

%define major	4
%define api	1.0
%define libname		%mklibname %{name}- %{api} %{major}
%define libname_basic	%mklibname %{name}-%{api}
%define dev	%{_lib}%{name}-devel
%define staticdev	%{_lib}%{name}-static-devel
%define minimal_libname		%mklibname %{name}-minimal- %{api} 0
%define minimal_libname_basic	%mklibname %{name}-minimal-%{api}

Summary:	Utilities belonging to the Reiser4 filesystem
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Kernel and hardware
Source0:	%{name}-%{version}.tar.bz2
Patch1:		reiser4progs-1.0.4-gcc4.patch
URL:		http://www.namesys.com/
BuildRequires:	libaal-devel >= 1.0.4
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
# wants uuid
BuildRequires:	e2fsprogs-devel
Requires:	%{libname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch1 -p1 -b .gcc4

%build
# be very careful
%configure2_5x \
	--sbindir=/sbin \
	%{?debug:--enable-debug}

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post	-n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post	-n %{minimal_libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{minimal_libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
# COPYING contains information other than GPL text
%doc AUTHORS COPYING CREDITS README THANKS
/sbin/*
%{_mandir}/man*/*

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libreiser4-%{api}.so.*
%{_libdir}/librepair-%{api}.so.*

%files -n %{minimal_libname}
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libreiser4-minimal-%{api}.so.*

%files -n %{dev}
%defattr(-,root,root,-)
%doc BUGS ChangeLog TODO
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_datadir}/aclocal/*.m4

%files -n %{staticdev}
%defattr(-,root,root,-)
%{_libdir}/lib*.a

