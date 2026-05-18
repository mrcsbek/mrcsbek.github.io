---
title: "Tailscale + Pi-hole on Raspberry Pi: No Ads Anywhere"
date: 2026-05-18
draft: false
tags: ["tailscale", "pihole", "raspberry-pi", "linux", "self-hosting"]
---

I wanted two things: route all my traffic through my home network,
and block ads at the DNS level everywhere I go. Here's how I did it
with a Raspberry Pi running Debian.

## What We're Building

- **Raspberry Pi** as a home server
- **Pi-hole** for network-wide ad blocking
- **Tailscale** to tunnel all traffic through home when away

The result: wherever I am, my internet exits from home — with zero ads.

## Requirements

- Raspberry Pi (any model with 512MB+ RAM)
- Debian or Raspberry Pi OS installed
- A Tailscale account (free)

## Step 1 — Install Pi-hole

```bash
curl -sSL https://install.pi-hole.net | bash
```

Follow the installer. When asked for upstream DNS, pick any (we'll
use Tailscale's DNS later). Note the admin password at the end.

## Step 2 — Install Tailscale

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up --advertise-exit-node
```

The `--advertise-exit-node` flag tells Tailscale this device can
route traffic for other devices.

## Step 3 — Enable Exit Node in Tailscale Admin

Go to [tailscale.com/admin](https://tailscale.com/admin), find your
Raspberry Pi and enable it as an exit node.

## Step 4 — Point Tailscale DNS to Pi-hole

In Tailscale admin → DNS → add your Pi's Tailscale IP as a
nameserver. Enable "Override local DNS".

Now all your devices on Tailscale use Pi-hole automatically.

## Step 5 — Connect From Any Device

On your phone or laptop:

```bash
sudo tailscale up --exit-node=<your-pi-tailscale-ip>
```

That's it. All traffic now routes through your Pi — with Pi-hole
blocking ads along the way.

## Result

Wherever I am, my internet looks like I'm home. No ads. No tracking.
One Raspberry Pi doing all the work.
