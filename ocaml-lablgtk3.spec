#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)
#
# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9 
%undefine	with_ocaml_opt
%endif

%define		ocaml_ver	1:3.09.2
Summary:	GTK+3 binding for OCaml
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla
Name:		ocaml-lablgtk3
Version:	3.1.1
Release:	0.1
License:	LGPL with linking exceptions
Group:		Libraries
Source0:	https://github.com/garrigue/lablgtk/archive/%{version}/lablgtk-%{version}.tar.gz
# Source0-md5:	c55c37b3ff0eaa2563f07a3fe01f9243
URL:		http://lablgtk.forge.ocamlcore.org/
BuildRequires:	gtk+3-devel
BuildRequires:	gtkspell3-devel
BuildRequires:	gtksourceview3-devel
BuildRequires:	ocaml-camlp4 >= %{ocaml_ver}
BuildRequires:	ocaml-dune
BuildRequires:	ocaml-cairo2-devel >= 0.6
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+3 binding for OCaml. This package contains files needed to run
bytecode OCaml programs using LablGtk.

%description -l pl.UTF-8
Wiązania GTK+3 dla OCamla. Pakiet ten zawiera binaria potrzebne do
uruchamiania programów używających LablGtk.

%package devel
Summary:	GTK+3 binding for OCaml - development part
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
GTK+3 binding for OCaml. This package contains files needed to develop
OCaml programs using LablGtk.

%description devel -l pl.UTF-8
Wiązania GTK+3 dla OCamla. Pakiet ten zawiera pliki niezbędne do
tworzenia programów używających LablGtk.

%package gtkspell
Summary:	GTK+3 binding for OCaml - GtkSpell support
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla - obsługa GtkSpella
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description gtkspell
GTK+3 binding for OCaml, GtkSpell support.

%description gtkspell -l pl.UTF-8
Wiązania GTK+3 dla OCamla, obsługa GtkSpella

%package gtkspell-devel
Summary:	GTK+3 binding for OCaml - GtkSpell support, development part
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla - obsługa GtkSpella, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gtkspell = %{version}-%{release}
%requires_eq	ocaml

%description gtkspell-devel
GTK+3 binding for OCaml, GtkSpell support. This package contains files
needed to develop OCaml programs using LablGtk-GtkSpell.

%description gtkspell-devel -l pl.UTF-8
Wiązania GTK+3 dla OCamla, obsługa GtkSpella. Ten pakiet zawiera pliki
niezbędne do tworzenia programów używających LablGtk-GtkSpell.

%package gtksourceview
Summary:	GTK+3 binding for OCaml - GtkSourceView support
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla - wsparcie dla GtkSourceView
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description gtksourceview
GTK+3 binding for OCaml, GtkSourceView support. This package contains
files needed to run bytecode OCaml programs using
LablGtk-GtkSourceView.

%description gtksourceview -l pl.UTF-8
Wiązania GTK+3 dla OCamla, wsparcie dla GtkSourceView. Pakiet ten
zawiera binaria potrzebne do uruchamiania programów używających
LablGtk-GtkSourceView.

%package gtksourceview-devel
Summary:	GTK+3 binding for OCaml - GtkSourceView support, development part
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla - wsparcie dla GtkSourceView, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gtksourceview = %{version}-%{release}
%requires_eq	ocaml

%description gtksourceview-devel
GTK+3 binding for OCaml, GtkSourceView support. This package contains
files needed to develop OCaml programs using LablGtk-GtkSourceView.

%description gtksourceview-devel -l pl.UTF-8
Wiązania GTK+3 dla OCamla, wsparcie dla GtkSourceView. Pakiet ten
zawiera pliki niezbędne do tworzenia programów używających
LablGtk-GtkSourceView.

%prep
%setup -q -n lablgtk-%{version}

%build
dune build %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/stublibs,%{_examplesdir}/%{name}-%{version}}

dune install --destdir=$RPM_BUILD_ROOT

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%dir %{_libdir}/ocaml/lablgtk3
%{_libdir}/ocaml/lablgtk3/lablgtk3.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk3/lablgtk3.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk3_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3/g[ABCDEFLMOPRTUW]*.cmi
%{_libdir}/ocaml/lablgtk3/gaux.cmi
%{_libdir}/ocaml/lablgtk3/gdk*.cmi
%{_libdir}/ocaml/lablgtk3/glib.cmi
%{_libdir}/ocaml/lablgtk3/gobject.cmi
%{_libdir}/ocaml/lablgtk3/gpointer.cmi
%{_libdir}/ocaml/lablgtk3/gtk.cmi
%{_libdir}/ocaml/lablgtk3/gtk[ABDEFILMNOPRTW]*.cmi
%{_libdir}/ocaml/lablgtk3/gtkSignal.cmi
%{_libdir}/ocaml/lablgtk3/gtkStock.cmi
%{_libdir}/ocaml/lablgtk3/gutf8.cmi
%{_libdir}/ocaml/lablgtk3/ogtk*.cmi
%{_libdir}/ocaml/lablgtk3/pango*.cmi
%{_libdir}/ocaml/lablgtk3/liblablgtk3_stubs.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk3/g[ABCDEFLMOPRTUW]*.cmx
%{_libdir}/ocaml/lablgtk3/gaux.cmx
%{_libdir}/ocaml/lablgtk3/gdk*.cmx
%{_libdir}/ocaml/lablgtk3/glib.cmx
%{_libdir}/ocaml/lablgtk3/gobject.cmx
%{_libdir}/ocaml/lablgtk3/gpointer.cmx
%{_libdir}/ocaml/lablgtk3/gtk.cmx
%{_libdir}/ocaml/lablgtk3/gtk[ABDEFILMNOPRTW]*.cmx
%{_libdir}/ocaml/lablgtk3/gtkSignal.cmx
%{_libdir}/ocaml/lablgtk3/gtkStock.cmx
%{_libdir}/ocaml/lablgtk3/gutf8.cmx
%{_libdir}/ocaml/lablgtk3/ogtk*.cmx
%{_libdir}/ocaml/lablgtk3/pango*.cmx
%{_libdir}/ocaml/lablgtk3/lablgtk3.a
%{_libdir}/ocaml/lablgtk3/lablgtk3.cmxa
%endif
%{_libdir}/ocaml/lablgtk3/gdk_tags.h
%{_libdir}/ocaml/lablgtk3/gtk_tags.h
%{_libdir}/ocaml/lablgtk3/ml_*.h
%{_libdir}/ocaml/lablgtk3/pango_tags.h
%{_libdir}/ocaml/lablgtk3/wrappers.h
%{_examplesdir}/%{name}-%{version}

%files gtkspell
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk3_gtkspell3_stubs.so

%files gtkspell-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3-gtkspell3/gtkSpell.cmi
%{_libdir}/ocaml/lablgtk3-gtkspell3/liblablgtk3_gtkspell3_stubs.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk3-gtkspell3/gtkSpell.cmx
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.a
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cmxa
%endif

%files gtksourceview
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk3_sourceview3_stubs.so

%files gtksourceview-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3-sourceview3/gSourceView3.cmi
%{_libdir}/ocaml/lablgtk3-sourceview3/gtkSourceView3.cmi
%{_libdir}/ocaml/lablgtk3-sourceview3/sourceView3Enums.cmi
%{_libdir}/ocaml/lablgtk3-sourceview3/liblablgtk3_sourceview3_stubs.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk3-sourceview3/gSourceView3.cmx
%{_libdir}/ocaml/lablgtk3-sourceview3/gtkSourceView3.cmx
%{_libdir}/ocaml/lablgtk3-sourceview3/sourceView3Enums.cmx
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.a
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cmxa
%endif
