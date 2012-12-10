Name: drakcowsay
Version: 0.7
Release: %mkrel 5
Summary: Graphical interface for cowsay
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Toys
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://peoples.mandriva.com/~blino/drakcowsay/
Requires: drakxtools cowsay
BuildRequires: xchat-devel

%description
%{name} is a graphical interface for cowsay.
Its target audience is those not yet familiar with the tough command line,
thus making cowsay rendering as easy as if you were a true l33t.

This package also includes drakcowthink, a graphical interface to cowthink.

%package -n xchat-%{name}
Group: System/Libraries
Summary: Xchat plugin for %{name}
Requires: xchat

%description -n xchat-%{name}
xchat-%{name} is a plugin for xchat to cowsay in your current IRC window.

%package -n irssi-%{name}
Group: System/Libraries
Summary: Irssi plugin for %{name}
Requires: irssi

%description -n irssi-%{name}
irssi-%{name} is a plugin for irssi to cowsay in your current IRC window.

%prep
%setup -q

%build
gcc -Wl,--export-dynamic -Wall -O1 -shared -fPIC -I. xchat-%{name}.c -o xchat-%{name}.so

%install
rm -rf %{buildroot}
install -m755 -D %{name} %{buildroot}%{_bindir}/%{name}
ln -s %{name} %{buildroot}%{_bindir}/drakcowthink
install -m755 -D xchat-%{name}.so %{buildroot}%{_libdir}/xchat/plugins/xchat-%{name}.so
install -m755 -D irssi-%{name}.pl %{buildroot}%{_datadir}/irssi/scripts/irssi-%{name}.pl

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/drakcowthink

%files -n xchat-%{name}
%defattr(-,root,root)
%{_libdir}/xchat/plugins/xchat-%{name}.so

%files -n irssi-%{name}
%defattr(-,root,root)
%{_datadir}/irssi/scripts/irssi-%{name}.pl


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7-5mdv2011.0
+ Revision: 617899
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.7-4mdv2010.0
+ Revision: 428337
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.7-3mdv2009.0
+ Revision: 244525
- rebuild
- fix summary-not-capitalized
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.7-1mdv2008.1
+ Revision: 124208
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - Import drakcowsay



* Sun Jun 18 2006 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2007.0
- new release 0.7:
  o fix release critical bug making this tool crash at startup
- mkrel
- update URL

* Wed Jun  1 2005 Claudio Matsuoka <claudio@mandriva.com> 0.6-2mdk
- added missing drakcowthink symlink
- fixed buildrequires to xchat-devel
- minor specfile cleanup

* Wed Oct 27 2004 Olivier Blin <blino@mandrake.org> 0.6-1mdk
- new release 0.6 :
  o parental advisory option (obscene cows are hidden by default)
  o read from stdin with '-' option

* Fri Aug 13 2004 Olivier Blin <blino@mandrake.org> 0.5-1mdk
- new release 0.5 :
  o remove ads in irc plugins
  o read initial input from command line or stdin

* Tue Jul 27 2004 Olivier Blin <blino@mandrake.org> 0.4-1mdk
- new release 0.4 (l33t edition):
  o irssi plugin

* Tue Jul 27 2004 Olivier Blin <blino@mandrake.org> 0.3-1mdk
- new release 0.3 (irc edition):
  o send to irc button
  o xchat plugin
  o word-wrap can be toggled
- redde rafaela quae sunt rafaela (fix changelog)

* Tue Jul 20 2004 Olivier Blin <blino@mandrake.org> 0.2-1mdk
- new release 0.2:
  o use scrollbars and resize TextViews
  o sort cows, quit button (rafael)
  o quit button (rafael)
  o misc fixes (rafael)
- requires cowsay (anne)

* Mon Jul 19 2004 Olivier Blin <blino@mandrake.org> 0.1-1mdk
- initial Mandrakelinux release
