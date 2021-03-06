# -*- mode: rpm-spec -*-

Summary: 	GTK+ DocBook Documentation Generator
Name: 		gtk-doc
Version: 	1.15
Release: 	1
License: 	GPL
Group: 		Utilities/Text
Source:	 	ftp://ftp.gtk.org/pub/gtk/v1.1/docs/rdp/gtk-doc-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-%{version}-root
URL: 		http://www.gtk.org/rdp/
BuildArchitectures: noarch
Requires: 	openjade
Requires:	perl >= 5.6.0
Requires:	libxslt
Requires:	docbook-dtds
Requires:	docbook-style-xsl
Provides:	perl(gtkdoc-common.pl)

BuildRequires: perl, openjade, libxslt, docbook-dtds, docbook-style-xsl

%description
gtk-doc is a set of perl scripts that generate API reference documention in
DocBook format.  It can extract documentation from source code comments in a
manner similar to java-doc.  It is used to generate the documentation for
GLib, Gtk+, and GNOME.

%prep
%setup -q

# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure $MYARCH_FLAGS  --prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} --datadir=%{_datadir}

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} \
     sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}  \
     datadir=$RPM_BUILD_ROOT%{_datadir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog README doc/* examples
# INSTALL is generic instructions from autoconf
# NEWS is currently empty
# %doc INSTALL
%doc NEWS

%{_bindir}/*
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%dir %{_datadir}/gtk-doc/data
%{_datadir}/gtk-doc/data/*
%{_libdir}/pkgconfig/*

%changelog
* Tue Jun 03 2003 Matthias Clasen <maclas@gmx.de>
- Add a missing Provides: and include the .pc file.  
  (#106568, Joe Pranevich)

* Sun Aug 12 2001 Jens Finke <jens@gnome.org>
- Modified to match GPP standard:
 - Changed to Copyright to License
 - Don't use hardcoded path, use rpm macros instead
 - Moved ChangeLog to the end of the file.
 - Removed packager
 - Don't set docdir path.
 - Use /var/tmp as installation prefix

* Fri Apr 27 2001 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Merge in some of the features of the redhat spec file.

* Wed Nov 15 2000 John Gotts <jgotts@linuxsavvy.com>
- Minor updates for 0.4.
* Thu Aug 26 1999 John E. Gotts <jgotts@engin.umich.edu>
- Created spec file.







