Name:		consul-utils
Version:	0.1.0
Release:	1%{?dist}
Summary:	Command line tools for Consul

Group:		Applications/System
License:	ASL 2.0
Source0:	https://github.com/CiscoCloud/consulacl/releases/download/v0.1.0/consulacl_0.1.0_linux_amd64.tar.gz
Source1:	https://github.com/CiscoCloud/consulkv/releases/download/v0.1.0/consulkv_0.1.0_linux_amd64.tar.gz

%description
Command line tools for Consul

%prep
%setup -T -b 0 -n consulacl_0.1.0_linux_amd64
%setup -T -b 1 -n consulkv_0.1.0_linux_amd64

%install
mkdir -p %{buildroot}/%{_bindir}
cp consulkv %{buildroot}/%{_bindir}
cd ../consulacl_0.1.0_linux_amd64
cp consulacl %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%attr(755, root, root) %{_bindir}/consulkv
%attr(755, root, root) %{_bindir}/consulacl
