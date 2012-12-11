%define _disable_ld_no_undefined 1

%define major	4
%define api	1.0
%define libname		%mklibname %{name}- %{api} %{major}
%define libname_basic	%mklibname %{name}-%{api}
%define dev	%{_lib}%{name}-devel
%define staticdev	%{_lib}%{name}-static-devel
%define minimal_libname		%mklibname %{name}-minimal- %{api} 0
%define minimal_libname_basic	%mklibname %{name}-minimal-%{api}

Summary:	Utilities belonging to the Reiser4 filesystem
Name:		reiser4progs
Version:	1.0.7
Release:	5
License:	GPL
Group:		System/Kernel and hardware
Source0:	%{name}-%{version}.tar.bz2
Patch0:		reiser4progs-1.0.7-fix-string-format.patch
URL:		http://www.namesys.com/
BuildRequires:	libaal-static-devel >= 1.0.5-4
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
%configure2_5x \
	--sbindir=/sbin \
	--libdir=/%{_lib} \
	--libexecdir=/%{_lib} \
	%{?debug:--enable-debug}

%make

%install
%makeinstall_std

%files
%defattr(-,root,root,-)
# COPYING contains information other than GPL text
%doc AUTHORS COPYING CREDITS README THANKS
/sbin/*
%{_mandir}/man*/*

%files -n %{libname}
%defattr(-,root,root,-)
%doc COPYING
/%{_lib}/libreiser4-%{api}.so.*
/%{_lib}/librepair-%{api}.so.*

%files -n %{minimal_libname}
%defattr(-,root,root,-)
%doc COPYING
/%{_lib}/libreiser4-minimal-%{api}.so.*

%files -n %{dev}
%defattr(-,root,root,-)
%doc BUGS ChangeLog TODO
/%{_lib}/lib*.so
%{_includedir}/*
%{_datadir}/aclocal/*.m4

%files -n %{staticdev}
%defattr(-,root,root,-)
/%{_lib}/lib*.a



%changelog
* Fri Aug 13 2010 Tomas Kindl <supp@mandriva.org> 1.0.7-4mdv2011.0
+ Revision: 569326
- rebuild for 2011.0/cooker

* Fri May 01 2009 Thomas Backlund <tmb@mandriva.org> 1.0.7-3mdv2010.0
+ Revision: 369995
- libs should be in /lib instead of /usr/lib (#50451)

* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.7-2mdv2009.1
+ Revision: 347944
- rebuild for latest readline

* Sun Feb 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.7-1mdv2009.1
+ Revision: 340579
- BuildRequires: glibc-static-devel in addition to libaal-static-devel
- Update to version 1.0.7
- Remove gcc4 patch: not needed anymore
- Added patch to fix string format errors
- Don't link with --no-undefined, it breaks the build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Feb 06 2008 Makoto Dei <makoto@turbolinux.co.jp> 1.0.4-1mdv2008.1
+ Revision: 163044
- build fix with gcc4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - remove old obsoletes that are useless for nearly 3 years
    - use %%mkrel
    - import reiser4progs


* Sat Mar 12 2005 Abel Cheung <deaddog@mandrake.org> 1.0.4-1mdk
- 1.0.4
- Remove all patches (upstream)
- Simplify description
- Fix mklibname
- Don't add maj to devel package, they are not parallel installable
- Split minimal library

* Sat Jan 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.3-1mdk
- 1.0.3
- new (lowered??) major
- fix provides

* Tue Jun 18 2004 Svetoslav Slavtchev <svetljo@gmx.de> 0.5.5-1mdk
- 0.5.5
- re-add static package

* Sat Jun 12 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.5.4-1thac
- Built for Mandrake 10.0 official

