Name:		fbg2
Version:	0.4
Release:	%mkrel 1
Summary:	Tetris clone
Group:		Games/Arcade
# Code is GPLv2+, music and graphics are CC-BY-SA
License:	GPLv2+ and CC-BY-SA
URL:		http://sourceforge.net/projects/fbg/
Source0:	http://downloads.sourceforge.net/project/fbg/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
BuildRequires:	radius-engine-devel >= 0.7
BuildRequires:	desktop-file-utils

%description
Falling Block Game is a free, open source block stacking game. The object of
the game is to move and rotate pieces in order to fill in complete rows. The
more rows you clear at once, the more points you score!

%prep
%setup -q
chmod -x License.txt ChangeLog *.c

%build
%configure
%make

%install
%makeinstall_std
%__mkdir_p %{buildroot}%{_datadir}/pixmaps/
%__install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/

%__mkdir_p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE2}

%files
%defattr(-,root,root,-)
%doc License.txt ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

