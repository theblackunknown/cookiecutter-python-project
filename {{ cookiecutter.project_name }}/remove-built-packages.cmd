
setlocal

rem Add git commit hash to built packages

@for %%G IN (%~dp0modules\module-{{ cookiecutter.project_name }} %~dp0applications\application-{{ cookiecutter.project_name }}) do (
    pushd %%G
    rmdir /S /Q dist build 2>NUL
    @popd
)
