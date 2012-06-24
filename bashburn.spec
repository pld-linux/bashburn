Summary:	BashBurn - burning CDs at console
Summary(pl):	BashBurn - nagrywanie p�yt pod konsol�
Name:		bashburn
%define	_name BashBurn  
Version:	1.6
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/bashburn/%{name}-%{version}.tar.gz
# Source0-md5:	6a1bd27162641bf47357749f118eb0f7
URL:		http://bashburn.sourceforge.net/
Requires:	cdrdao
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
Obsoletes:	BashBurn
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BashBurn is a bash script designed to make CD burning at the console
easier. It supports burning normal data CDs, audio CDs, blanking
CD-RWs, multisession, and more.

%description -l pl
BashBurn to skrypt w bashu zaprojektowany aby u�atwi� nagrywanie p�yt
CD pod konsol�. Umo�liwia nagrywanie CD z normalnymi danymi, p�yt
audio, czyszczenie CD-RW, wielosesyjno�� i wi�cej.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{_name}/{burning,config,convert,lang/English,lang/Polish,menus,misc},%{_sysconfdir}}
install burning/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/burning
install config/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/config
install convert/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/convert
install lang/English/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/lang/English
install lang/Polish/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/lang/Polish
install menus/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/menus
install misc/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/misc
install BashBurn.sh $RPM_BUILD_ROOT%{_bindir}/bashburn
sed "s|%{_prefix}/local|%{_datadir}|" bashburnrc > $RPM_BUILD_ROOT%{_sysconfdir}/bashburnrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/bashburn
%attr(755,root,root) %{_datadir}/%{_name}
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/bashburnrc
