Name:           iasl
Version:        20090123
Release:        3.1%{?dist}
Summary:        Intel ASL compiler/decompiler

Group:          Development/Languages
License:        Intel ACPI
URL:            http://developer.intel.com/technology/iapc/acpi/ 
Source0:        http://www.acpica.org/download/acpica-unix-%{version}.tar.gz
Source1:        iasl-README.Fedora
Source2:        http://ftp.debian.org/debian/pool/main/a/acpica-unix/acpica-unix_20060912-3.2.diff.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  bison patchutils flex


%description
iasl compiles ASL (ACPI Source Language) into AML (ACPI Machine Language),
which is suitable for inclusion as a DSDT in system firmware. It also can
disassemble AML, for debugging purposes.


%prep
%setup -q -n acpica-unix-%{version}
cp -p %{SOURCE1} README.Fedora
zcat %{SOURCE2} |  filterdiff -i \*iasl.1  | patch -p2


%build
export CC=gcc
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$CFLAGS"
cd compiler
# does not compile with %{?_smp_mflags}
make


%install
rm -rf $RPM_BUILD_ROOT
install -p -D compiler/iasl $RPM_BUILD_ROOT%{_bindir}/iasl
install -m 0644 -p -D iasl.1 $RPM_BUILD_ROOT%{_mandir}/man1/iasl.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc changes.txt README README.Fedora
%{_bindir}/iasl
%{_mandir}/man1/iasl.1.gz


%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20090123-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090123-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090123-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Till Maas <opensource@till.name> - 20090123-1
- Update to new upstream release

* Sat Dec 20 2008 Till Maas <opensource@till.name> - 20081203-1
- Update to new upstream release
- Update Source0

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 20061109-4
- Autorebuild for GCC 4.3

* Sat Aug 11 2007 Till Maas <opensource till name> - 20061109-3
- update License Tag to new Guidelines
- rebuild because of #251794

* Tue Feb 20 2007 Till Maas <opensource till name> - 20061109-2
- Make description line less than 80 instead of less that 81 characters long
- Permissions of manpage are 0644 instead of 0755 now

* Thu Feb 01 2007 Till Maas <opensource till name> - 20061109-1
- initial spec for Fedora Extras
