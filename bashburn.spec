Summary:	BashBurn - burning CDs at console
Summary(pl):	BashBurn - nagrywanie p³yt pod konsol±
Name:		BashBurn
Version:	1.5.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/bashburn/%{name}-%{version}.tar.gz
# Source0-md5:	b34ce2ac8c74794032adf13a5bf5cd1d
URL:		http://bashburn.sourceforge.net
Requires:	/bin/bash
Requires:	cdrdao
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BashBurn is a bash script designed to make CD burning at the console
easier. It supports burning normal data CDs, audio CDs, blanking
CD-RWs, multisession, and more.

%description -l pl
BashBurn to skrypt w bashu zaprojektowany aby u³atwiæ nagrywanie p³yt
CD pod konsol±. Umo¿liwia nagrywanie CD z normalnymi danymi, p³yt
audio, czyszczenie CD-RW, wielosesyjno¶æ i wiêcej.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/{burning,config,convert,lang/English,menus,misc},%{_sysconfdir}}
install burning/* $RPM_BUILD_ROOT%{_datadir}/%{name}/burning
install config/* $RPM_BUILD_ROOT%{_datadir}/%{name}/config
install convert/* $RPM_BUILD_ROOT%{_datadir}/%{name}/convert
install lang/English/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lang/English
install menus/* $RPM_BUILD_ROOT%{_datadir}/%{name}/menus
install misc/* $RPM_BUILD_ROOT%{_datadir}/%{name}/misc
install BashBurn.sh $RPM_BUILD_ROOT%{_bindir}/bashburn
sed "s|%{_prefix}/local|%{_datadir}|" bashburnrc > $RPM_BUILD_ROOT%{_sysconfdir}/bashburnrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/bashburn
%attr(755,root,root) %{_datadir}/%{name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/bashburnrc
