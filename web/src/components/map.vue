<template>
    <div class="map" id="map"></div>
</template>

<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=9qq1nm76rr"></script>
<script>
import axios from "axios"

export default {
    name: 'nmap',
    data() {
        return {
        userLatitude: null,
        userLongtitude: null,
        map:null,
        }
    },
    methods:{
        mapinit: function(initLat,initLng){
            console.log("MAP INITIALIZING...");
            let mapDiv = document.getElementById('map');
            let mapOptions = {
            center: new naver.maps.LatLng(initLat, initLng),
            zoom: 16
            };
            let map = new naver.maps.Map(mapDiv, mapOptions);
            this.map = map
            console.log("INITIALIZED:",this.map)
            console.log("GEOLOCATION:",initLat,initLng)
            
            
            // console.log(mapDiv)
            // console.log("POSITION: ",pos.coords.latitude,pos.coords.longitude)
            
        },
        getMarketsData() {
            axios.get("http://127.0.0.1:5000/markets")
            .then(res => {
                console.log("result:",res.data)
                return res.data
            })
            .catch(err => {
                console.log(err)
            })
            
        },
        async markOnMap(map){
            let bounds = map.getBounds(),
                southWest = bounds.getSW(),
                northEast = bounds.getNE(),
                lngSpan = northEast.lng() - southWest.lng(),
                latSpan = northEast.lat() - southWest.lat();
            const markets = await this.getMarketsData(),
                marketsNum = await markets.length;
            
            await console.log("ARRAY:",markets)

            for (let i=0; i<(marketsNum);i++) {
                let position = new naver.maps.LatLng(markets[i][2],markets[i][3]);

                let marker = new naver.maps.Marker({
                    map: map,
                    position: position,
                    title: key,
                    icon: {
                        path: [2],
                        style: "CIRCLE",
                        size: new naver.maps.Size(24, 37),
                        anchor: new naver.maps.Point(12, 37),
                        origin: new naver.maps.Point(markets[i][2], markets[i][3])
                    },
                    zIndex: 100
                });

                markers.push(marker);
            };
        }
    },
    mounted() {
        navigator.geolocation.getCurrentPosition(async pos => {
            this.currentUserLocation  = {userLatitude: pos.coords.latitude, userLongtitude : pos.coords.longitude};
            this.userLatitude = pos.coords.latitude
            this.userLongtitude = pos.coords.longitude
            // console.log("currentUserLocation.userLatitude:",currentUserLocation.userLatitude);
            // console.log("currentUserLocation.userLongtitude:", currentUserLocation.userLongtitude);
            await this.mapinit(pos.coords.latitude, pos.coords.longitude);
            
            
        },
        error => {
            console.log(error.message);
        },
        {enableHighAccuracy: true}
        );
        navigator.geolocation.watchPosition(pos => {
            let markerOptions = {
                position: new naver.maps.LatLng(pos.coords.latitude, pos.coords.longitude),
                map: this.map,
                icon: {
                    url: 'https://ssl.pstatic.net/static/maps/m/pin_rd.png',
                    scaledSize: new naver.maps.Size(20, 20),
                    origin: new naver.maps.Point(0, 0),
                    anchor: new naver.maps.Point(25, 26)
                }
            };
            let marker = new naver.maps.Marker(markerOptions);
        },error => {
            console.log(error.message);
        },
        {enableHighAccuracy: true})
        // this.markOnMap(map);
        

        // 아이스크림콘 아이콘
        // let markerOptions = {
            
        //     position: new naver.maps.LatLng(pos.coords.latitude, pos.coords.longitude),
        //     map: map,
        //     SymbolIcon: {
        //         path: [2],
        //         style: "CIRCLE",
        //         size: new naver.maps.Size(50, 52),
        //         origin: new naver.maps.Point(0, 0),
        //         anchor: new naver.maps.Point(25, 26)
        //     }
        // };

        
    },
    updated(){
        console.log(this.data)
        
        
    },
    watch: {
        
    }
}
</script>

<style lang="scss" scoped>
.map {  
    margin: auto;
    padding-top: 20%;
    height: 100%;
    width: 100%;
}    
   
</style>