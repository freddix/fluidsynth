Summary:	RT synthesizer
Name:		fluidsynth
Version:	1.1.6
Release:	5
License:	LGPL
Group:		Applications/Sound
Source0:	http://downloads.sourceforge.net/fluidsynth/%{name}-%{version}.tar.gz
# Source0-md5:	ae5aca6de824b4173667cbd3a310b263
URL:		http://www.fluidsynth.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	gdbm-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	json-c-devel
BuildRequires:	ladspa-devel
BuildRequires:	libasyncns-devel
BuildRequires:	libogg-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	pkg-config
#BuildRequires:	pulseaudio-devel
BuildRequires:	xorg-libXi-devel
BuildRequires:	xorg-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fluid Synth is a software, real-time synthesizer based on the
Soundfont 2 specifications.

%package devel
Summary:	Development files for the FluidSynth
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files necessary to develop
applications using FluidSynth.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure \
	--disable-ladcca	\
	--disable-lash		\
	--disable-static	\
	--enable-jack-support	\
	--enable-ladspa		\
	--enable-midishare
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.?
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.la
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_pkgconfigdir}/fluidsynth.pc

