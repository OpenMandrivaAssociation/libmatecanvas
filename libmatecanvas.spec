%define api	2
%define major	0
%define libname	%mklibname matecanvas %{api} %{major}
%define devname %mklibname -d matecanvas

Summary:	GnomeCanvas widget
Name:		libmatecanvas
Version:	1.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}/%{name}-%{version}.tar.xz

BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: pkgconfig(gail)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libart-2.0)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(pango) >= 1.0.1
BuildRequires: pkgconfig(pangoft2) >= 1.0.1

%description
The MATE canvas is an engine for structured graphics that offers a rich
imaging model, high performance rendering, and a powerful, high-level API.
It offers a choice of two rendering back-ends, one based on Xlib for
extremely fast display, and another based on Libart, a sophisticated,
antialiased, alpha-compositing engine. Applications have a choice between
the Xlib imaging model or a superset of the PostScript imaging model,
depending on the level of graphic sophistication required.

%package -n %{libname}
Summary:	%{summary}
Group:		%{group}
Suggests:	%{name} >= %{version}

%description -n %{libname}
This package contains the main canvas library.


%package -n %{devname}
Summary:	Development libraries and include files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{devname}
This package contains development library and header files for %{name}.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--enable-glade

%make

%install
%makeinstall_std

%{find_lang} %{name}

%files  -f %{name}.lang

%files -n %{libname}
%{_libdir}/libmatecanvas-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog NEWS README AUTHORS
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/lib*.so
# mate says to enable glade
%{_libdir}/libglade/2.0/libgladematecanvas.so
%{_libdir}/pkgconfig/*



%changelog
* Fri Jul 27 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.4.0-1
+ Revision: 811356
- new version 1.4.0

* Thu May 31 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 801608
- imported package libmatecanvas

