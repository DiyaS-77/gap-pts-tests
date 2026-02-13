syntax = "proto3";

service PTSTrigger {
  rpc RunProject(ProjectRequest) returns (stream TestOutput);
  rpc GetReport(ProjectRequest) returns (ReportFile);
}

message ProjectRequest {
  string config = 1;
  string testbed = 2;
  string workspace = 3;
  string project = 4;
}

message TestOutput {
  string line = 1;
}

message ReportFile {
  string filename = 1;
  bytes content = 2;
}
