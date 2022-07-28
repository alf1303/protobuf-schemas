pub mod wavesmy {
    tonic::include_proto!("wavesmy");

    pub mod events {
        tonic::include_proto!("wavesmy.events");

        pub mod grpc {
            tonic::include_proto!("wavesmy.events.grpc");
        }
    }

    pub mod node {
        pub mod grpc {
            tonic::include_proto!("wavesmy.node.grpc");
        }
    }
}
