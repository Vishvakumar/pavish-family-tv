# PaVish Family TV

Curated IPTV playlist for the PaVish family — 46 channels across UK, Tamil, Malayalam, Kids, Music, and News.

## Playlist URL

```
https://raw.githubusercontent.com/Vishvakumar/pavish-family-tv/main/playlist.m3u
```

## EPG (TV Guide) URLs

```
https://iptv-org.github.io/epg/guides/gb.xml
https://iptv-org.github.io/epg/guides/in.xml
```

---

## Kodi + PVR IPTV Simple Client (Fire TV Cube)

### Step 1 — Install Kodi

1. On your Fire TV Cube, open the **App Store**
2. Search for **Kodi** and install it
3. Open Kodi

### Step 2 — Install PVR IPTV Simple Client

1. In Kodi, go to **Settings** (gear icon) → **Add-ons**
2. Tap **Install from repository** → **Kodi Add-on repository**
3. Go to **PVR clients** → **PVR IPTV Simple Client**
4. Tap **Install** and wait for it to complete

### Step 3 — Configure the playlist

1. Go to **Settings → Add-ons → My add-ons → PVR clients → PVR IPTV Simple Client**
2. Tap **Configure**
3. Under **General**:
   - Set **M3U playlist location** to **Remote path (Internet address)**
   - Paste the playlist URL:
     ```
     https://raw.githubusercontent.com/Vishvakumar/pavish-family-tv/main/playlist.m3u
     ```

### Step 4 — Configure EPG (TV Guide)

1. Still in PVR IPTV Simple Client settings, go to the **EPG Settings** tab
2. Set **XMLTV URL** to:
   ```
   https://iptv-org.github.io/epg/guides/gb.xml
   ```
3. Tap **OK** to save

> For Indian channel guide data, add a second EPG source via **Settings → PVR & Live TV → Guide → Add**:
> `https://iptv-org.github.io/epg/guides/in.xml`

### Step 5 — Enable Live TV

1. Go back to the Kodi home screen
2. You should see a **TV** section appear in the menu
3. Kodi will prompt you to enable the PVR add-on — tap **Enable**
4. Wait for it to scan channels (~30 seconds)

### Step 6 — Browse channels

- Go to **TV → Channels** to see all channels
- Channels are grouped: **Favourites, UK, Tamil, Malayalam, Kids, Music, News**
- Go to **TV → Guide** to see the EPG programme schedule

---

## Channel List (46 channels)

| Group | Channels |
|-------|---------|
| Favourites | BBC One HD, Star Vijay HD, Asianet, CBeebies HD, BBC News, Al Jazeera English |
| UK | BBC One HD, BBC Two HD, BBC Three HD, BBC Four HD, BBC News, ITV1, ITV2 HD, Channel 5, Sky News, GB News |
| Tamil | Star Vijay HD, Kalaignar TV, Jaya TV HD, Jaya Max, Colors Tamil HD, Zee Tamil News, Isai Aruvi, DD Tamil |
| Malayalam | Asianet, Mazhavil Manorama, Flowers TV, Amrita TV, Kaumudy TV, Janam TV, Asianet News, Manorama News, Mathrubhumi News, DD Malayalam |
| Kids | CBeebies HD, CBBC HD, Disney Junior, Nick HD+, Nickelodeon, Nick Jr. |
| Music | 9XM, MTV India, B4U Music, Music India |
| News | NDTV 24x7, NDTV India, India Today, Aaj Tak, ABP News, Al Jazeera English, France 24 English, DW English, Euronews English |

---

## Troubleshooting

**Channel not loading?**
Community-maintained public streams occasionally go offline. Check [iptv-org/iptv](https://github.com/iptv-org/iptv) for updated URLs and edit `playlist.m3u` in this repo.

**No EPG / guide data showing?**
In Kodi go to **Settings → PVR & Live TV → Guide** and tap **Update guide**. EPG data may take a few minutes to load after first setup.

**Want to update the channel list?**
Edit `playlist.m3u` directly in this repo. Kodi will pick up changes on next scheduled refresh (or force it via **Settings → PVR & Live TV → General → Refresh interval**).

---

*Stream sources from [iptv-org/iptv](https://github.com/iptv-org/iptv) — community maintained.*
