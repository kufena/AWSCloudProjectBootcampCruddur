using System.Net;
using Amazon.Lambda.Core;
using Amazon.Extensions.Configuration.SystemsManager;
using System.Text.Json;
using Microsoft.Extensions.Configuration;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace SignupLambda;

public class Functions
{

    string? Connection_String { get; init; }
    /// <summary>
    /// Default constructor that Lambda will invoke.
    /// </summary>
    public Functions()
    {
        var configurations = new ConfigurationBuilder()
                        .AddSystemsManager("/cruddur/")
                        .AddAppConfigUsingLambdaExtension("AppConfigApplicationId", "AppConfigEnvironmentId", "AppConfigConfigurationProfileId")
                        .Build();
        Connection_String = configurations["postgres-connection-string"];
    }


    /// <summary>
    /// A lambda to respond to the sign up - post confirmation - stage in cognito.
    /// </summary>
    /// <param name="request"></param>
    /// <returns>Json object?</returns>
    public async Task<JsonElement> FunctionHandler(JsonElement input, ILambdaContext context)
{
    var request = input.GetProperty("request");
    var userAttributes = request.GetProperty("userAttributes");
    string? email = userAttributes.GetProperty("email").GetString();
    string? user_cognito_id = userAttributes.GetProperty("sub").GetString();
    string? display_name = userAttributes.GetProperty("name").GetString();
    string? handle = userAttributes.GetProperty("preferred_username").GetString();

    if (Connection_String is null) {
        throw new Exception("no connection string found.");
    }

    using (UserDbContext db = new UserDbContext(Connection_String)) {
        UserModel um = new UserModel(email, user_cognito_id, display_name, handle);
        if (db.Users != null) db.Users.Add(um);

        db.SaveChanges();
        Console.WriteLine($"New uuid is {um.uuid}");
    }
    return input;
}
}