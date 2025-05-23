use std::sync::LazyLock;

use anyhow::Result;
use async_trait::async_trait;
use tokio::sync::RwLock;

use chirpstack_api::gw;

use super::GatewayBackend;

static DOWNLINK_FRAMES: LazyLock<RwLock<Vec<gw::DownlinkFrame>>> =
    LazyLock::new(|| RwLock::new(Vec::new()));
static GATEWAY_CONFIGURATIONS: LazyLock<RwLock<Vec<gw::GatewayConfiguration>>> =
    LazyLock::new(|| RwLock::new(Vec::new()));

pub async fn reset() {
    DOWNLINK_FRAMES.write().await.drain(..);
    GATEWAY_CONFIGURATIONS.write().await.drain(..);
}

pub struct Backend {}

#[async_trait]
impl GatewayBackend for Backend {
    async fn send_downlink(&self, df: &chirpstack_api::gw::DownlinkFrame) -> Result<()> {
        DOWNLINK_FRAMES.write().await.push(df.clone());
        Ok(())
    }

    async fn send_configuration(
        &self,
        gw_conf: &chirpstack_api::gw::GatewayConfiguration,
    ) -> Result<()> {
        GATEWAY_CONFIGURATIONS.write().await.push(gw_conf.clone());
        Ok(())
    }
}

pub async fn get_downlink_frames() -> Vec<gw::DownlinkFrame> {
    DOWNLINK_FRAMES.write().await.drain(..).collect()
}

pub async fn get_gateway_configurations() -> Vec<gw::GatewayConfiguration> {
    GATEWAY_CONFIGURATIONS.write().await.drain(..).collect()
}
