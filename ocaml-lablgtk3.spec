#
# Conditional build:
%bcond_without	ocaml_opt	# skip building native optimized binaries (bytecode is always built)
#
# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} arm aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

%define		ocaml_ver	1:4.05.0
Summary:	GTK+3 binding for OCaml
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla
Name:		ocaml-lablgtk3
Version:	3.1.1
Release:	4
License:	LGPL with linking exceptions
Group:		Libraries
Source0:	https://github.com/garrigue/lablgtk/archive/%{version}/lablgtk-%{version}.tar.gz
# Source0-md5:	c55c37b3ff0eaa2563f07a3fe01f9243
URL:		http://lablgtk.forge.ocamlcore.org/
BuildRequires:	camlp5
BuildRequires:	gtk+3-devel >= 3.18
BuildRequires:	gtksourceview3-devel
BuildRequires:	gtkspell3-devel
BuildRequires:	help2man
BuildRequires:	ocaml-cairo2-devel >= 0.6
BuildRequires:	ocaml-dune >= 1.8
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
Requires:	%{name}-tools = %{version}-%{release}
Requires:	ocaml-cairo2-devel >= 0.6
%requires_eq ocaml

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
%requires_eq ocaml-runtime

%description gtkspell
GTK+3 binding for OCaml, GtkSpell support.

%description gtkspell -l pl.UTF-8
Wiązania GTK+3 dla OCamla, obsługa GtkSpella

%package gtkspell-devel
Summary:	GTK+3 binding for OCaml - GtkSpell support, development part
Summary(pl.UTF-8):	Wiązania GTK+3 dla OCamla - obsługa GtkSpella, część programistyczna
Group:		Development/Libraries
Requires:	%{name}-gtkspell = %{version}-%{release}
%requires_eq ocaml

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
%requires_eq ocaml

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
%requires_eq ocaml

%description gtksourceview-devel
GTK+3 binding for OCaml, GtkSourceView support. This package contains
files needed to develop OCaml programs using LablGtk-GtkSourceView.

%description gtksourceview-devel -l pl.UTF-8
Wiązania GTK+3 dla OCamla, wsparcie dla GtkSourceView. Pakiet ten
zawiera pliki niezbędne do tworzenia programów używających
LablGtk-GtkSourceView.

%package tools
Summary:	GTK+ binding for OCaml - tools
Summary(pl.UTF-8):	Wiązania GTK+ dla OCamla - narzędzia
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq ocaml

%description tools
GTK+ binding for OCaml. This package contains tools for working with
lablgtk.

%description tools -l pl.UTF-8
Wiązania GTK+ dla OCamla. Pakiet ten zawiera narzędzia do pracy z
lablgtk.

%prep
%setup -q -n lablgtk-%{version}

for p in lablgtk3 lablgtk3-gtkspell3 lablgtk3-sourceview3; do
	echo -e "\nversion: \"%{version}\"" >> ${p}.opam
done

%build
dune build %{?_smp_mflags}

help2man -N --version-string=%{version} -o gdk_pixbuf_mlsource3.1 _build/install/default/bin/gdk_pixbuf_mlsource3
help2man -N --version-string=%{version} -o lablgladecc3.1 _build/install/default/bin/lablgladecc3

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/ocaml/stublibs,%{_examplesdir}/%{name}-%{version}}

dune install --destdir=$RPM_BUILD_ROOT

cp -p gdk_pixbuf_mlsource3.1 lablgladecc3.1 $RPM_BUILD_ROOT%{_mandir}/man1

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk3*/*.ml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%dir %{_libdir}/ocaml/lablgtk3
%{_libdir}/ocaml/lablgtk3/META
%{_libdir}/ocaml/lablgtk3/lablgtk3.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk3/lablgtk3.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk3_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3/*.cmi
%{_libdir}/ocaml/lablgtk3/*.cmt
%{_libdir}/ocaml/lablgtk3/*.cmti
%{_libdir}/ocaml/lablgtk3/*.mli
%{_libdir}/ocaml/lablgtk3/liblablgtk3_stubs.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk3/*.cmx
%{_libdir}/ocaml/lablgtk3/lablgtk3.a
%{_libdir}/ocaml/lablgtk3/lablgtk3.cmxa
%endif
%{_libdir}/ocaml/lablgtk3/gdk_tags.h
%{_libdir}/ocaml/lablgtk3/gtk_tags.h
%{_libdir}/ocaml/lablgtk3/ml_*.h
%{_libdir}/ocaml/lablgtk3/pango_tags.h
%{_libdir}/ocaml/lablgtk3/wrappers.h
%{_libdir}/ocaml/lablgtk3/dune-package
%{_libdir}/ocaml/lablgtk3/opam
%{_examplesdir}/%{name}-%{version}

%files gtkspell
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/lablgtk3-gtkspell3
%{_libdir}/ocaml/lablgtk3-gtkspell3/META
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk3_gtkspell3_stubs.so

%files gtkspell-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmi
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmt
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmti
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.mli
%{_libdir}/ocaml/lablgtk3-gtkspell3/liblablgtk3_gtkspell3_stubs.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk3-gtkspell3/*.cmx
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.a
%{_libdir}/ocaml/lablgtk3-gtkspell3/lablgtk3_gtkspell3.cmxa
%endif
%{_libdir}/ocaml/lablgtk3-gtkspell3/dune-package
%{_libdir}/ocaml/lablgtk3-gtkspell3/opam

%files gtksourceview
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/lablgtk3-sourceview3
%{_libdir}/ocaml/lablgtk3-sourceview3/META
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk3_sourceview3_stubs.so

%files gtksourceview-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmi
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmt
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmti
%{_libdir}/ocaml/lablgtk3-sourceview3/*.mli
%{_libdir}/ocaml/lablgtk3-sourceview3/liblablgtk3_sourceview3_stubs.a
%if %{with ocaml_opt}
%{_libdir}/ocaml/lablgtk3-sourceview3/*.cmx
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.a
%{_libdir}/ocaml/lablgtk3-sourceview3/lablgtk3_sourceview3.cmxa
%endif
%{_libdir}/ocaml/lablgtk3-sourceview3/dune-package
%{_libdir}/ocaml/lablgtk3-sourceview3/opam

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdk_pixbuf_mlsource3
%attr(755,root,root) %{_bindir}/lablgladecc3
%{_mandir}/man1/gdk_pixbuf_mlsource3.1*
%{_mandir}/man1/lablgladecc3.1*
