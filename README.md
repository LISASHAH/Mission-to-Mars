# Mission-to-Mars

<html>

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="ie=edge" />
  <title>Mission to Mars</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
</head>

<body>
  <div class="container">
    <div class="jumbotron text-center">
      <h1>Mission to Mars</h1>
      <p><a class="btn btn-primary btn-lg" href="/scrape" role="button">Scrape New Data</a></p>
    </div>

    <!-- Mars News -->
    <div class="row" id="mars-news">
      <div class="col-md-12">
        <div class="media">
          <div class="media-body">
            <h2>Latest Mars News</h2>
            <h4 class="media-heading">Nine Finalists Chosen in NASA&#39;s Mars 2020 Rover Naming Contest</h4>
            <p>Nine finalists have been chosen in the essay contest for K-12 students across U.S. to name NASA&#39;s next Mars rover. Now you can help by voting for your favorite. </p>
          </div>
        </div>
      </div>
    </div>
    <!-- Mars Featured Image -->
    <div class="row" id="mars-featured-image">
      <div class="col-md-8">
        <h2>Featured Mars Image</h2>
        <img src="https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA18291_hires.jpg" class="img-responsive" alt="Responsive image">
      </div>
      <div class="col-md-4">
        <!-- Mars Facts -->
        <div class="row" id="mars-facts">
          <div class="col-md-12">
            <h4>Mars Facts</h4>
            <table border="1" class="dataframe">  <thead>    <tr style="text-align: right;">      <th>description</th>      <th>value</th>    </tr>    <tr>      <th></th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Equatorial Diameter:</th>      <td>6,792 km</td>    </tr>    <tr>      <th>Polar Diameter:</th>      <td>6,752 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.39 × 10^23 kg (0.11 Earths)</td>    </tr>    <tr>      <th>Moons:</th>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>Orbit Distance:</th>      <td>227,943,824 km (1.38 AU)</td>    </tr>    <tr>      <th>Orbit Period:</th>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>Surface Temperature:</th>      <td>-87 to -5 °C</td>    </tr>    <tr>      <th>First Record:</th>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>Recorded By:</th>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>
          </div>
        </div>
      </div>
    </div>
    <h2 class='text-center'><strong> Mars Hemispheres</strong></h2>
    <hr>
    <div class="row" id="mars-hem1">
      <div class="col-lg-6 text-right">
        <img src=http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg alt="hemi1" class='borderbox' style="width:400px;height:400px;" />
        <p class='h4 text-center'>Cerberus Hemisphere Enhanced</p>
      </div>
      <div class="col-lg-6 text-left">
        <img src=http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg alt="hemi2" class='borderbox' style="width:400px;height:400px;" />
        <p class='h4 text-center'>Schiaparelli Hemisphere Enhanced</p>
      </div>
    </div>
    <div class="row" id="mars-hem2">
      <div class="col-lg-6 text-right">
        <img src=http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg alt="hemi3" class='borderbox' style="width:400px;height:400px;" />
        <p class='h4 text-center'>Syrtis Major Hemisphere Enhanced</p>
      </div>
      <div class="col-lg-6 text-left">
        <img src=http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg alt="hemi4" class='borderbox'
          style="width:400px;height:400px;" />
        <p class='h4 text-center'>Valles Marineris Hemisphere Enhanced</p>
      </div>
    </div>

  </div>
</body>
</html>
