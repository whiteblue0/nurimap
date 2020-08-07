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
            currentUserLocation: {
            userLatitude: null,
            userLongtitude: null,
            },
        map:null,
        }
    },
    methods:{
       updateMarkers(map, markers) {

            let mapBounds = map.getBounds();
            let marker, position;

            for (let i = 0; i < markers.length; i++) {

                marker = markers[i]
                position = marker.getPosition();

                if (mapBounds.hasLatLng(position)) {
                    showMarker(map, marker);
                } else {
                    hideMarker(map, marker);
                }
            }
        },
        showMarker(map, marker) {

            if (marker.getMap()) return;
            marker.setMap(map);
        },
        hideMarker(map, marker) {

            if (!marker.getMap()) return;
            marker.setMap(null);
        } 
    },
    created(){
        
    },
    mounted() {
        navigator.geolocation.watchPosition(pos => {
            // 
            let userLatitude =  pos.coords.latitude
            let userLongtitude = pos.coords.longitude
            let mapDiv = document.getElementById('map');
            let mapOptions = {
            center: new naver.maps.LatLng(userLatitude, userLongtitude),
            zoom: 16
            };
            let map = new naver.maps.Map(mapDiv, mapOptions);
            this.map = map
            let HOME_PATH = window.HOME_PATH || '.';
            let MARKER_SPRITE_X_OFFSET = 29,
                MARKER_SPRITE_Y_OFFSET = 50,
                MARKER_SPRITE_POSITION = {
                    "A0": [0, 0],
                    "B0": [MARKER_SPRITE_X_OFFSET, 0],
                    "C0": [MARKER_SPRITE_X_OFFSET*2, 0],
                    "D0": [MARKER_SPRITE_X_OFFSET*3, 0],
                    "E0": [MARKER_SPRITE_X_OFFSET*4, 0],
                    "F0": [MARKER_SPRITE_X_OFFSET*5, 0],
                    "G0": [MARKER_SPRITE_X_OFFSET*6, 0],
                    "H0": [MARKER_SPRITE_X_OFFSET*7, 0],
                    "I0": [MARKER_SPRITE_X_OFFSET*8, 0],

                    "A1": [0, MARKER_SPRITE_Y_OFFSET],
                    "B1": [MARKER_SPRITE_X_OFFSET, MARKER_SPRITE_Y_OFFSET],
                    "C1": [MARKER_SPRITE_X_OFFSET*2, MARKER_SPRITE_Y_OFFSET],
                    "D1": [MARKER_SPRITE_X_OFFSET*3, MARKER_SPRITE_Y_OFFSET],
                    "E1": [MARKER_SPRITE_X_OFFSET*4, MARKER_SPRITE_Y_OFFSET],
                    "F1": [MARKER_SPRITE_X_OFFSET*5, MARKER_SPRITE_Y_OFFSET],
                    "G1": [MARKER_SPRITE_X_OFFSET*6, MARKER_SPRITE_Y_OFFSET],
                    "H1": [MARKER_SPRITE_X_OFFSET*7, MARKER_SPRITE_Y_OFFSET],
                    "I1": [MARKER_SPRITE_X_OFFSET*8, MARKER_SPRITE_Y_OFFSET],

                    "A2": [0, MARKER_SPRITE_Y_OFFSET*2],
                    "B2": [MARKER_SPRITE_X_OFFSET, MARKER_SPRITE_Y_OFFSET*2],
                    "C2": [MARKER_SPRITE_X_OFFSET*2, MARKER_SPRITE_Y_OFFSET*2],
                    "D2": [MARKER_SPRITE_X_OFFSET*3, MARKER_SPRITE_Y_OFFSET*2],
                    "E2": [MARKER_SPRITE_X_OFFSET*4, MARKER_SPRITE_Y_OFFSET*2],
                    "F2": [MARKER_SPRITE_X_OFFSET*5, MARKER_SPRITE_Y_OFFSET*2],
                    "G2": [MARKER_SPRITE_X_OFFSET*6, MARKER_SPRITE_Y_OFFSET*2],
                    "H2": [MARKER_SPRITE_X_OFFSET*7, MARKER_SPRITE_Y_OFFSET*2],
                    "I2": [MARKER_SPRITE_X_OFFSET*8, MARKER_SPRITE_Y_OFFSET*2]
                };
            
            let bounds = map.getBounds(),
                southWest = bounds.getSW(),
                northEast = bounds.getNE(),
                lngSpan = northEast.lng() - southWest.lng(),
                latSpan = northEast.lat() - southWest.lat();

            let markers = [];

            for (let key in MARKER_SPRITE_POSITION) {

                let position = new naver.maps.LatLng(
                    southWest.lat() + latSpan * Math.random(),
                    southWest.lng() + lngSpan * Math.random());

                let marker = new naver.maps.Marker({
                    map: map,
                    position: position,
                    title: key,
                    icon: {
                        url: "https://ssl.pstatic.net/static/maps/m/pin_rd.png",
                        size: new naver.maps.Size(24, 37),
                        anchor: new naver.maps.Point(12, 37),
                        origin: new naver.maps.Point(MARKER_SPRITE_POSITION[key][0], MARKER_SPRITE_POSITION[key][1])
                    },
                    zIndex: 100
                });

                markers.push(marker);
            };
            naver.maps.Event.addListener(map, 'idle', function() {
            this.updateMarkers(map, markers);
        });
            
        },
        error => {
            console.log(error.message);
        },
        {enableHighAccuracy: true}
        );
        

        

        
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