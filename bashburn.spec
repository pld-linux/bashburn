%define		_name	BashBurn
Summary:	BashBurn - burning CDs at console
Summary(pl):	BashBurn - nagrywanie p³yt pod konsol±
Name:		bashburn
Version:	1.7.1
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/bashburn/%{_name}-%{version}.tar.gz
# Source0-md5:	612ab3cae4e96f32c83691b0d4b82d8d
URL:		http://bashburn.sourceforge.net/
Requires:	cdrdao
Requires:	cdrecord
Requires:	cdda2wav
Requires:	mkisofs
Obsoletes:	BashBurn
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BashBurn is a bash script designed to make CD & DVD burning at the
console easier. It supports burning normal data CDs, audio CDs,
blanking CD-RWs, multisession, and more.

To use DVD burning you have to install:
- dvdrtools

%description -l pl
BashBurn to skrypt w bashu zaprojektowany aby u³atwiæ nagrywanie p³yt
CD z poziomu terminala tekstowego. Umo¿liwia nagrywanie CD i DVD z
normalnymi danymi, p³yt audio, czyszczenie CD-RW, wielosesyjno¶æ i
wiêcej.

Aby nagrywaæ DVD, nale¿y zainstalowaæ:
- dvdrtools

%prep
%setup -q -n %{_name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{_name}/{burning,config,convert,menus,misc},%{_sysconfdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/%{_name}/lang/{Czech,English,German,Norwegian,Polish,Spanish,Swedish}

for lng in lang/* ; do
	install $lng/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/$lng
done
install burning/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/burning
install config/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/config
install convert/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/convert
install menus/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/menus
install misc/* $RPM_BUILD_ROOT%{_datadir}/%{_name}/misc
install BashBurn.sh $RPM_BUILD_ROOT%{_bindir}/bashburn
sed "s|/usr/local|%{_datadir}|" bashburnrc > $RPM_BUILD_ROOT%{_sysconfdir}/bashburnrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/bashburn
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bashburnrc
%dir %{_datadir}/%{_name}
%attr(755,root,root) %{_datadir}/%{_name}/burning
%attr(755,root,root) %{_datadir}/%{_name}/config
%attr(755,root,root) %{_datadir}/%{_name}/convert
%attr(755,root,root) %{_datadir}/%{_name}/menus
%attr(755,root,root) %{_datadir}/%{_name}/misc
%dir %{_datadir}/%{_name}/lang
%{_datadir}/%{_name}/lang/English
%lang(cz) %{_datadir}/%{_name}/lang/Czech
%lang(de) %{_datadir}/%{_name}/lang/German
%lang(es) %{_datadir}/%{_name}/lang/Spanish
%lang(nb) %{_datadir}/%{_name}/lang/Norwegian
%lang(pl) %{_datadir}/%{_name}/lang/Polish
%lang(sv) %{_datadir}/%{_name}/lang/Swedish
