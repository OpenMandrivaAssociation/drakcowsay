Name: drakcowsay
Version: 0.7
Release: %mkrel 4
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
