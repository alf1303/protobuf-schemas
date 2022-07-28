fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::configure().compile(
        &[
            "proto/wavesmy/node/grpc/accounts_api.proto",
            "proto/wavesmy/node/grpc/assets_api.proto",
            "proto/wavesmy/node/grpc/blockchain_api.proto",
            "proto/wavesmy/node/grpc/blocks_api.proto",
            "proto/wavesmy/node/grpc/transactions_api.proto",
            "proto/wavesmy/events/events.proto",
            "proto/wavesmy/events/grpc/blockchain_updates.proto",
        ],
        &["proto"],
    )?;

    Ok(())
}
