python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/emojifier.proto
cd D:\Projs\emojifier\emojifier\src\cs\GUI
packages\Grpc.Tools.1.11.0\tools\windows_x86\protoc.exe -I../../../protos --csharp_out=. --grpc_out=. ../../../protos/emojifier.proto --plugin=protoc-gen-grpc=packages\Grpc.Tools.1.11.0\tools\windows_x86\grpc_csharp_plugin.exe