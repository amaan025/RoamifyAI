// map.js
let map;
let manchester = { lat: 53.4808, lng: -2.2426 }; // Coordinates for Manchester city center

function initMap() {
    // Map configuration
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: manchester,
        mapTypeId: 'roadmap',
        disableDefaultUI: false,
        gestureHandling: 'cooperative',
        styles: [
            {
                featureType: "poi",
                elementType: "labels",
                stylers: [{ visibility: "off" }]
            },
            {
                featureType: "transit",
                elementType: "labels",
                stylers: [{ visibility: "off" }]
            }
        ]
    });

    // Custom marker
    new google.maps.Marker({
        position: manchester,
        map: map,
        title: "Manchester City Center",
        icon: {
            path: google.maps.SymbolPath.CIRCLE,
            scale: 8,
            fillColor: "#764ba2",
            fillOpacity: 1,
            strokeWeight: 2,
            strokeColor: "white"
        }
    });

    // Map load verification
    google.maps.event.addListenerOnce(map, 'tilesloaded', () => {
        if (!document.getElementById("map").children.length) {
            showMapError();
        }
    });

    // Window resize handler
    window.addEventListener('resize', handleResize);
}

function handleResize() {
    if (map) {
        setTimeout(() => {
            google.maps.event.trigger(map, 'resize');
            map.setCenter(manchester);
        }, 300);
    }
}

function showMapError() {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'alert alert-danger mt-3';
    errorDiv.innerHTML = `
        <h4>Map Failed to Load</h4>
        <p>Please check your internet connection and try refreshing the page.</p>
        <small>If the problem persists, contact support@roamify.com</small>
    `;
    document.getElementById("map").replaceWith(errorDiv);
}

// Google Maps API error handling
window.gm_authFailure = function() {
    showMapError();
};

// Initialize map when DOM loads
document.addEventListener('DOMContentLoaded', () => {
    if (typeof google !== 'undefined') {
        initMap();
    } else {
        showMapError();
    }
});