Name:		opencl-filesystem
Version:	1.0
Release:	1%{?dist}
Summary:	OpenCL filesystem layout

Group:		System Environment/Libraries
License:	Public Domain
URL:		http://www.khronos.org/registry/cl/

BuildArch:	noarch


%description
This package provides some directories required by packages which use OpenCL.


%prep


%install
# ICD Loader Vendor Enumeration
# http://www.khronos.org/registry/cl/extensions/khr/cl_khr_icd.txt
mkdir -p %{buildroot}/%{_sysconfdir}/OpenCL/vendors/


%files
%{_sysconfdir}/OpenCL/


%changelog
* Wed Aug 28 2013 Fabian Deutsch <fabiand@fedoraproject.org> - 1.0-1
- Initial package
