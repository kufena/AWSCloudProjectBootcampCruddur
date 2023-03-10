using Microsoft.EntityFrameworkCore;

namespace SignupLambda;

public class UserDbContext : DbContext
{
    string connectionString { get; set; } = "";
    public UserDbContext(string connString) : base() 
    {
        connectionString = connString;
    }

    public DbSet<UserModel>? Users { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseNpgsql(connectionString);
    }
}
