# CateOrDoge
Code for a website that contains image classifier. Deployed using Flask on Heroku, styled with Bootstrap

<h1>Thank you for taking interest in this website! </h1> 

This website was created with Flask and hosted on Heroku. Classifies the image you upload, and tells you whether the image you have uploaded is a cat or a dog, amongst other things. 
<p>
  Step 1: Upload your image (png / jpg / jpeg) to the website
  Step 2: Use either ResNetV250 or MobileNetV2 (with transfer learning) to predict your image 
  Step 3: The website will update the background image, and return what it thinks the iamge contains (In the case of ResNetV2: tabby, humming bird etc)
</p>

<h6>Additional Comments</h6> 
I used transfer learning on MobileNetV2 and added additional layers to the model. While the main model remained untrained, I trained the added layers on cifar10. 
Hence, the MobileNetV2 option return 10 classes which are airplanes, cars, birds, cats, deer, dogs, frogs, horses, ships, and trucks. 