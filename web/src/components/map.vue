<template>
    <div class="map" id="map"></div>
</template>

<script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=9qq1nm76rr"></script>
<script>
export default {
    name: 'nmap',
    data: () => {
        return {
            currentUserLocation: {
            userLatitude: null,
            userLongtitude: null
        }
        }
    },
    methods:{

    },
    mounted() {
        navigator.geolocation.getCurrentPosition(async pos => {
            this.currentUserLocation  = {userLatitude: pos.coords.latitude, userLongtitude : pos.coords.longitude};
            console.log("currentUserLocation.userLatitude:",this.currentUserLocation.userLatitude);
            console.log("currentUserLocation.userLongtitude:",this.currentUserLocation.userLongtitude);
            let  mapOptions = await {
            center: new naver.maps.LatLng(pos.coords.latitude, pos.coords.longitude),
            zoom: 16
            };
            let mapDiv = await document.getElementById('map');
            let map = await new naver.maps.Map(mapDiv, mapOptions);
            // console.log(mapDiv)
            // console.log("POSITION: ",pos.coords.latitude,pos.coords.longitude)
            let markerOptions = await {
                position: new naver.maps.LatLng(pos.coords.latitude, pos.coords.longitude),
                map: map,
                icon: {
                    url: 'https://ssl.pstatic.net/static/maps/m/pin_rd.png',
                    scaledSize: new naver.maps.Size(20, 20),
                    origin: new naver.maps.Point(0, 0),
                    anchor: new naver.maps.Point(25, 26)
                }
            };

            // 아이스크림콘 아이콘
            // let markerOptions = await {
                
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

            let marker = await new naver.maps.Marker(markerOptions);
        },
        error => {
            console.log(error.message);
        }
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